# python3


def max_pairwise_product(numbers):
    # print('in function')
    s = 1
    if len(numbers) >= 2:
        large1 = max(numbers)
        numbers.remove(large1)
        large2 = max(numbers)
        return large1 * large2
    else:
        for i in numbers:
            s = i * s
            return s


if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    if n == len(input_numbers):
        print(max_pairwise_product(input_numbers))
