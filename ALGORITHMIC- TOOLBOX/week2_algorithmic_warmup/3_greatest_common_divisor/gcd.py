# Uses python3
import sys


def gcd_naive(a, b):
    if b == 0:
        return a
    else:
        return gcd_naive(b, a % b)


if __name__ == "__main__":
    my = list(map(int, input().split()))
    a = max(my)
    b = min(my)
    print(gcd_naive(a, b))
