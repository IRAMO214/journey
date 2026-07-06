import threading
import time
import random

def worker(name):
    print(f"{name} Started")
    time.sleep(random.randint(1,5))
    print(f"{name} Finished")

threads = []

for i in range(5):
    t = threading.Thread(target=worker, args=(f"Thread-{i}",))

threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print("Finished")