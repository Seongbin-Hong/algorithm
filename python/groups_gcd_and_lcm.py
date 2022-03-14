def gcd_two_numbers(larger: int, smaller: int) -> int:
    if larger < smaller:
        temp = larger
        larger = smaller
        smaller = temp

    if larger % smaller == 0:
        return smaller
    else:
        return gcd_two_numbers(smaller, larger % smaller)


def gcd_number_groups(numbers: list) -> int:
    numbers_gcd = numbers[0]

    for index in range(len(numbers)):
        if index == 0:
            continue

        numbers_gcd = gcd_two_numbers(numbers_gcd, numbers[index])

    return numbers_gcd


def lcm_numbers_groups(numbers: list) -> int:
    numbers_lcm = numbers[0]
    numbers_gcd = numbers[0]

    for index in range(len(numbers)):
        if index == 0:
            continue

        numbers_gcd = gcd_two_numbers(numbers_lcm, numbers[index])
        numbers_lcm = (numbers_lcm * numbers[index]) // numbers_gcd

    return numbers_lcm


def common_divisor(gcd: int) -> list:
    return [x for x in range(1, gcd + 1) if gcd % x == 0]


T = int(input())

for index in range(T):
    U = int(input())
    V = str(input())

    numbers = [int(x) for x in V.split(" ")]

    numbers_gcd = gcd_number_groups(numbers)
    numbers_lcm = lcm_numbers_groups(numbers)
    common_divisors = common_divisor(numbers_gcd)

    print(numbers_lcm)
    print(numbers_gcd)
    print(common_divisors)
