import time
from timeit import default_timer as timer
from multiprocessing import Pool, cpu_count
import numpy as np


def square(x, y):
    return x*y


def main():

    start = timer()

    print(f'starting computations on {cpu_count()} cores')
    size_a = 1080
    size_b = 1920
    values = []
    for x in range(size_a):
        for y in range(size_b):
            values += [[x, y]]

    with Pool() as pool:
        res = pool.starmap(square, values)
        print(res)

    end = timer()
    print(f'elapsed time: {end - start}')

if __name__ == '__main__':
    main()