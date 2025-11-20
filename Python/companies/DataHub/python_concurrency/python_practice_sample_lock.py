from threading import Lock, Thread
import time


if __name__ == "__main__":
    lock = Lock()
    shared_resource = 0

    def worker(id):
        global shared_resource
        print(f"Worker {id} is waiting for the lock")
        with lock:
            print(f"Worker {id} has acquired the lock")
            local_copy = shared_resource
            time.sleep(0.1)  # Simulate some processing
            local_copy += 1
            shared_resource = local_copy
            print(f"Worker {id} is releasing the lock")

    threads = []
    for i in range(5):
        t = Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Final value of shared resource: {shared_resource}")