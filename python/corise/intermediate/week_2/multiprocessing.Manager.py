import multiprocessing

def worker1(shared_dict):
    """Modify the shared dictionary"""
    shared_dict['msg'] = 'Hello World'

def worker2(shared_dict):
    """Read from the shared dictionary"""
    print(shared_dict['msg'])

if __name__ == '__main__':
    # Create a manager object to manage the shared dictionary
    manager = multiprocessing.Manager()

    # Create a shared dictionary
    shared_dict = manager.dict()

    # Create two processes to modify and read from the shared dictionary
    process1 = multiprocessing.Process(target=worker1, args=(shared_dict,))
    process2 = multiprocessing.Process(target=worker2, args=(shared_dict,))

    # Start the processes
    process1.start()
    process2.start()

    # Wait for the processes to finish
    process1.join()
    process2.join()