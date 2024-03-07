import time
import multiprocessing

def cpu_task(process_id):
    start_time = time.time()
    print(f'Process {process_id} started')
    result = sum(range(100_000_000))
    end_time = time.time()
    print(f'Process {process_id} finished, time:', end_time - start_time)
    return result

if __name__ == '__main__':
    print('Cores:', multiprocessing.cpu_count())

    print('Single task:')
    cpu_task(1)

    print('Multiprocessing pool:')
    processes = 1
    with multiprocessing.Pool(processes=processes) as pool:
        results = pool.map(cpu_task, [(i,) for i in range(processes)])
        print(results)