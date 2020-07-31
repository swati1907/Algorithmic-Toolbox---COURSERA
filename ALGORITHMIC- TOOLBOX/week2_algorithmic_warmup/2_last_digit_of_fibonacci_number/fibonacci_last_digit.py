# Uses python3
from typing import List


def calc_fib(n):
    number = [0,1]
    for i in range(2, n+1):
        m = number[i - 1]%10 + number[i - 2]%10
        number.append(m)
    b = number.pop()
    return b%10


n = int(input())
print(calc_fib(n))

