import threading
import time
import random

def philo(i, l, r, butler):
    while True:
        print(f"Philosopher {i} is thinking")
        time.sleep(random.randint(1, 2))

        print(f"Philosopher {i} is waiting")
        butler.acquire()

        l.acquire()
        r.acquire()

        print(f"Philosopher {i} is eating")
        time.sleep(random.randint(1, 2))

        r.release()
        l.release()
        butler.release()


n = 5

chopsticks = [threading.Lock() for _ in range(n) ]

butler = threading.Semaphore(n-1)

threads = []

for i in range(n):
    t = threading.Thread(
        target = philo,
        args = (i, chopsticks[i], chopsticks[(i+1)%n],butler )
        )
    threads.append(t)
    t.start()

