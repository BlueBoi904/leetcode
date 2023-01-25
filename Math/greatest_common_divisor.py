import math


def findGCD(nums: list[int]):
    # Find max and min num

    min_num = min(nums)
    max_num = max(nums)

    return math.gcd(min_num, max_num)

# Alt solution


def find_gcd(nums: list[int]):
    a, b = min(nums), max(nums)
    while a:
        a, b = b % a, a
    return b
