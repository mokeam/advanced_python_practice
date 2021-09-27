from threading import Thread, Lock, current_thread
from queue import Queue

def worker(q, lock):
    while True:
        value = q.get() # Blocks until the item is available

        with lock:
            print(f"in {current_thread().name} got {value}")
        
        q.task_done()

if __name__ == "__main__":
    q = Queue()
    num_threads = 10
    lock = Lock()

    for i in range(num_threads):
        thread = Thread(name = f"Thread{i+1}", target = worker, args = (q, lock))
        thread.daemon = True # Dies when the main thread dies
        thread.start()

    # Fill the queue with items
    for x in range(20):
        q.put(x)

    # Block until all items in the queue have been gotten and processed!
    q.join()

    print("Main done")