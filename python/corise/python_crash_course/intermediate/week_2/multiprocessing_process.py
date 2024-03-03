import multiprocessing
import time


def compute_product(n, worker_num):
    st = time.time()
    mul = 1
    for i in range(1, n):
        mul *= i
    en = time.time()

    print(f'Worker {worker_num} ran in {en-st} seconds')


def main():
    # Define the number of processes to run
    num_processes = 2

    # Create a list of processes to run
    processes = []
    for i in range(num_processes):
        p = multiprocessing.Process(target=compute_product, args=(100000, i))
        processes.append(p)

    # Start the processes
    for p in processes:
        p.start()

    # Wait for the processes to finish
    for p in processes:
        p.join()

    print('All processes are done')


if __name__ == '__main__':
    main()