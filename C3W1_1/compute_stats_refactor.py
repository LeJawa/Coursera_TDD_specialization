import math
from typing import List

file = 'random_nums.txt'

def read_ints() -> List[int]:
    data = []
    with open(file, 'r') as f:
        for line in f.readlines():
            data.append(int(line));
    return data

def count() -> int:
    data = read_ints()
    return len(data)

def summation() -> int:
    data = read_ints()
    return sum(data)

def average() -> float:
    return summation() / count()

def minimum() -> int:
    return min(read_ints())

def maximum() -> int:
    return max(read_ints())


def harmonic_mean() -> float:
    return count() / sum(1/x for x in read_ints())


def variance() -> float:
    mu = average()
    return sum([(x-mu)**2 for x in read_ints()]) / count()


def standard_dev() -> float:
    return math.sqrt(variance())


if __name__ == '__main__':
    print(read_ints())
    print(count())
    print(summation())
    print(average())
    print(minimum())
    print(maximum())
    print(harmonic_mean())
    print(variance())
    print(standard_dev())



