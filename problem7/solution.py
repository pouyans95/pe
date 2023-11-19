import math

def is_prime_number(number):
    """
    Check if a number is prime.

    Args:
        number (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
        
    Excluding even numbers before entering the loop can result in more efficient checking.
    Note that we are only checking odd numbers inside the loop by using 2 as the increasing step value.
    """
    if number < 2 or number % 2 == 0:
        return False
    if number == 2:
        return True
    
    sqrt = math.isqrt(number)
    return all(number % div != 0 for div in range(3, sqrt + 1, 2))

def solution(cnt):
    """
    Find the nth prime number.

    Args:
        cnt (int): The position of the prime number to find.

    Returns:
        int: The nth prime number.
    """
    current_cnt = 0
    current_num = 2

    while current_cnt < cnt:
        if is_prime_number(current_num):
            current_cnt += 1
        current_num += 1

    return current_num - 1

cnt = 10001
print(solution(cnt))
