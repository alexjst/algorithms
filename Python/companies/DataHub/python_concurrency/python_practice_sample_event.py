from threading import Event, Thread
import time


if __name__ == "__main__":
    event = Event()

    def waiter(id):
        print(f"Waiter {id} is waiting for the event to be set")
        event.wait()
        print(f"Waiter {id} detected the event is set and is proceeding")

    def setter():
        print("Setter is sleeping for 2 seconds before setting the event")
        time.sleep(2)
        event.set()
        print("Setter has set the event")

    threads = []
    for i in range(3):
        t = Thread(target=waiter, args=(i,))
        threads.append(t)
        t.start()

    setter_thread = Thread(target=setter)
    setter_thread.start()

    for t in threads:
        t.join()
    setter_thread.join()