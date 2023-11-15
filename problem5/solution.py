def get_gcd(num1, num2):
    """
    Calculate the greatest common divisor (GCD) of two numbers.
    Alternatively, you can use : from math import gcd
    Args:
        num1: The first number.
        num2: The second number.

    Returns:
        The GCD of num1 and num2.

    Examples:
        >>> gcd(12, 8)
        4
        >>> gcd(25, 15)
        5
    """
    if num1 == num2:
        return num1

    a = max(num1, num2)
    b = min(num1, num2)
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b


def get_lcm(num1, num2):
    return (num1*num2)//get_gcd(num1, num2)


num = 20
def solution():
    lcm = 2
    for i in range(3, num):
        lcm = get_lcm(lcm,i)
    return lcm

print(solution())