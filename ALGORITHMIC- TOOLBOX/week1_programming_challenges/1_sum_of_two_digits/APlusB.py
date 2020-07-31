# python3


def sum_of_two_digits(first_digit, second_digit):
    assert 0 <= first_digit <= 9 and 0 <= second_digit <= 9
    c=first_digit+second_digit
    return c


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(sum_of_two_digits(a, b))

