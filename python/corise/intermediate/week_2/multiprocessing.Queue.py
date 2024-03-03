import multiprocessing

def producer(queue):
    """Producer function to put items in the queue"""
    for i in range(5):
        print(f'Putting {i} in the queue')
        queue.put(i)

def consumer(queue):
    """Consumer function to get items from the queue"""
    while True:
        item = queue.get()
        if item is None:
            break
        print(f'Got {item} from the queue')

if __name__ == '__main__':
    # Create a queue to exchange data between the processes
    queue = multiprocessing.Queue()

    # Create a producer process to put items in the queue
    producer_process = multiprocessing.Process(target=producer, args=(queue,))

    # Create a consumer process to get items from the queue
    consumer_process = multiprocessing.Process(target=consumer, args=(queue,))

    # Start the processes
    producer_process.start()
    consumer_process.start()

    # Wait for the producer process to finish
    producer_process.join()

    # Add a None item to the queue to signal the consumer process to stop
    queue.put(None)

    # Wait for the consumer process to finish
    consumer_process.join()