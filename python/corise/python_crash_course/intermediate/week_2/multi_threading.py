# Multi-Threaded Python program
import time
from threading import Thread


def compute_product(n, n_thread):
    res = 1
    for i in range(1, n):
        res *= i

    print(f"Thread-{n_thread} computation done")


def main():
    threads = list()
    n_threads = 5
    n = 100000
    for n_thread in range(n_threads):
        threads.append(Thread(target=compute_product, args=(n,n_thread)))

    startTime = time.time()
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    endTime = time.time()

    print("Time taken", endTime - startTime)


if __name__ == '__main__':
    main()