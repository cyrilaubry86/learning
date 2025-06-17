import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds to run")
        return result
    return wrapper

@timeit
def my_func():
    for _ in range(10000000):
        pass

my_func()