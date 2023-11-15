def is_palindrome(s):
    return s == s[::-1]


def is_product_of_two_n_digit(number, digits):
    """
    Checks if the given number is a product of two n-digit numbers.

    Args:
        number (int): The number to check.
        digits (int): The number of digits for the n-digit numbers.

    Returns:
        bool: True if the number is a product of two n-digit numbers, False otherwise.

    """
    max_limit = 10**digits - 1
    min_limit = 10**(digits - 1)

    for div in range(max_limit, min_limit - 1, -1):
        if number % div == 0:
            quo = number // div
            if min_limit <= quo <= max_limit:
                return True

    return False



def solution(digits):
    """
    Finds the largest palindrome number that is a product of two n-digit numbers.

    Args:
        digits (int): The number of digits for the n-digit numbers.

    Returns:
        int: The largest palindrome number that is a product of two n-digit numbers.

    """
    for number in range((10**digits - 1)**2, (10**(digits-1))**2 - 1, -1):
        if is_palindrome(str(number)) and is_product_of_two_n_digit(number, digits):
            return number



print(solution(3))