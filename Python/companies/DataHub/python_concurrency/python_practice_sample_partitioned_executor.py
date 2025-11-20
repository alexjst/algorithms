from queue import Queue, Empty, Full
from threading import Thread, Event, Lock
from dataclasses import dataclass
from typing import Any

@dataclass
class Request:
    request_id: str
    partition_key: str
    payload: Any

class PartitionedRequestExecutor:
    def __init__(self, num_workers=4, max_queue_size_per_worker=100):
        self.num_workers = num_workers
        self.queues = [Queue(maxsize=max_queue_size_per_worker) for _ in range(num_workers)]
        self.workers = []
        self.shutdown_event = Event()
        self.metrics_lock = Lock()
        self.metrics = {
            "submitted" : 0,
            "rejected" : 0,
            "processed" : 0,
            "failed" : 0
        }
        
        for worker_id in range(num_workers):
            t = Thread(target=self._worker_loop, args = (worker_id, ))
            t.start()
            self.workers.append(t)
    
    def _worker_loop(self, worker_id):
        while not self.shutdown_event.is_set():
            try:
                request = self.queues[worker_id].get(block=True, timeout=0.5)
                try:
                    print(f"processed request {request.request_id} with partition {request.partition_key}")
                    with self.metrics_lock:
                        self.metrics["processed"] += 1
                except Exception as e:
                    print(f"error getting request in worker {worker_id}: {e}")
                    with self.metrics_lock:
                        self.metrics["failed"] += 1
                finally:
                    self.queues[worker_id].task_done()
            except Empty:
                continue
    
    def submit(self, request) -> bool:
        queue_id = hash(request.partition_key) % self.num_workers
        try:
            self.queues[queue_id].put(request, block=False)
            with self.metrics_lock:
                self.metrics["submitted"] += 1
            return True
        except Full:
            print(f"request with id {request.request_id} in partition {request.partition_key} rejected")
            with self.metrics_lock:
                self.metrics["rejected"] += 1
            return False
    
    def shutdown(self, wait=True):
        if wait:
            for q in self.queues:
                q.join()
        self.shutdown_event.set()
        for worker in self.workers:
            worker.join()
    
    def get_metrics(self):
        with self.metrics_lock:
            return self.metrics.copy()

if __name__ == "__main__":
    # build some requests
    executor = PartitionedRequestExecutor()
    names = ["aaa", "bbb", "ccc", "ddd"]
    for i in range(100):
        request = Request(i, partition_key=f"{names[i%4]}", payload=f"payload-{i}")
        executor.submit(request)
    executor.shutdown()
    metrics = executor.get_metrics()
    if metrics["submitted"] != metrics["processed"] + metrics["rejected"] + metrics["failed"]:
        print("metrics do not add up!")
    else:
        print("metrics are consistent:", metrics)
    