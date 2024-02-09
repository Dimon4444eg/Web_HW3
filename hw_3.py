from multiprocessing import Pool, cpu_count
import time


def factorize(*numbers):
    divisible_numbers_list = []
    for num in numbers:
        for i in range(1, num + 1):
            if num % i == 0:
                divisible_numbers_list.append(i)
    return divisible_numbers_list


if __name__ == '__main__':
    num_cpus = cpu_count()

    with Pool(num_cpus) as pool:
        start = time.time()
        result = pool.map(factorize, (128, 255, 99999, 10651060))
        end = time.time()
        work = end - start
        print(f"time process {work}")
        print(result)
        print("Number of CPUs:", num_cpus)
