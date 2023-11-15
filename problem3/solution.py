import math

def is_prime(x) -> bool:
    if x < 2:
        return False
    return all(x % i != 0 for i in range(2, int(math.isqrt(x)) + 1))

def solution(number):
    """
    Finds the largest prime factor of the given number.

    Args:
        number (int): The number to find the largest prime factor of.

    Returns:
        int: The largest prime factor of the given number.
    """

    return next((div for div in range(math.isqrt(number), 0, -1) if number % div == 0 and is_prime(div)), 0)


number = 600851475143
print (solution(number))
        