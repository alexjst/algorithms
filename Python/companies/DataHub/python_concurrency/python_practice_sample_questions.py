from queue import Queue
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed


if __name__ == "__main__":
    
    q = Queue(maxsize = 2)

    def producer(item):
        q.put(item, block=True, timeout=10)
        print(f"produced {item}")

    def consumer(id):
        item = q.get(block=True, timeout=10)
        print(f"consumed {item} from consumer {id}")
        q.task_done()

    with ThreadPoolExecutor(max_workers=4) as executor:
        producer_futures = [executor.submit(producer, i) for i in range(10)]
        consumer_futures = [executor.submit(consumer, i) for i in range(10)]

        # Wait for futures as they complete, not in submission order
        all_futures = producer_futures + consumer_futures
        for future in as_completed(all_futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error: {type(e).__name__}: {e}")
    
    while not q.empty():
        item = q.get()
        print(item)