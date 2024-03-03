import time


def compute_product(n):
    res = 1
    for i in range(1, n):
        res *= i
        
    #print(str(res))
    print(f"Computation done")


def main():
    startTime = time.time()
    compute_product(n=100000)
    endTime = time.time()

    print("Time taken", endTime - startTime)


if __name__ == '__main__':
    main()