import multiprocessing
import time


def compute_product(n, worker_num):
    st = time.time()
    mul = 1
    for i in range(1, n):
        mul *= i
    en = time.time()

    print(f'Worker {worker_num} ran in {en-st} seconds')
    return mul


def main_pool():
    with multiprocessing.Pool(processes=2) as pool:
        # Apply the worker function to each argument in the list in parallel
        results = pool.starmap(compute_product, [(100000, 0), (100000, 1)])

        # Close the pool and wait for all the tasks to complete
        pool.close()
        pool.join()
        print(results)

if __name__ == '__main__':
    main_pool()