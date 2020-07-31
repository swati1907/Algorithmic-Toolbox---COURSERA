# Uses python3
import sys
'''The least common multiple of two positive integers 𝑎 and 𝑏 is the least positive
integer 𝑚 that is divisible by both 𝑎 and 𝑏.
Problem Description
Task. Given two integers 𝑎 and 𝑏, find their least common multiple.
Input Format. The two integers 𝑎 and 𝑏 are given in the same line separated by space.
Constraints. 1 ≤ 𝑎, 𝑏 ≤ 107
.
Output Format. Output the least common multiple of 𝑎 and 𝑏.'''

def lcd_naive(a, b):
    if b == 0:
        return a
    else:
        return lcd_naive(b, a % b)


if __name__ == "__main__":
    my = list(map(int, input().split()))
    a = max(my)
    b = min(my)
    c = lcd_naive(a, b)
    print((a*b)//c )
