# Uses python3
from typing import List


def calc_fib(n):
    if n == 0 or n == 1:
        return n
    number = [0, 1]
    for i in range(2, n + 1):
        m = number[i - 1] + number[i - 2]
        number.append(m)
    b = number.pop()
    return b


n = int(input())
print(calc_fib(n))
