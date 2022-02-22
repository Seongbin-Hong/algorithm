from cgitb import small
from os import scandir

#

# Greatest Common Divisor


def gcd(larger: int, smaller: int) -> int:
    if not isinstance(larger, int) | isinstance(smaller, int):
        print("a or b argument is not integer.")

    if larger < smaller:
        temp = larger
        larger = smaller
        smaller = temp

    if larger % smaller == 0:
        return smaller
    else:
        return gcd(smaller, larger % smaller)


# Lowest Common Multiple
def lcm(larger: int, smaller: int) -> int:
    if not isinstance(larger, int) | isinstance(smaller, int):
        print("a or b argument is not integer.")

    if larger < smaller:
        temp = larger
        larger = smaller
        smaller = temp

    return larger * smaller // gcd(larger, smaller)


print(gcd(70, 30))
print(lcm(70, 30))
