MAX_VALUE = 4000000



def fibonacci(n, memo={}):  # sourcery skip: default-mutable-arg
    """
    Calculates the Fibonacci number at the given index.

    Args:
        n (int): The index of the Fibonacci number to calculate.

    Returns:
        int: The Fibonacci number at the given index.

    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(5)
        5
    """

    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]


def solution(max_value):
    """
    Calculates the sum of even Fibonacci numbers up to the given maximum value.

    Args:
        max_value (int): The maximum value up to which to calculate the sum.

    Returns:
        int: The sum of even Fibonacci numbers up to the given maximum value.
    """

    total = 0
    fib_index = 0

    while True:
        fib_val = fibonacci(fib_index)
        
        if fib_val > max_value:
            break

        if fib_val % 2 == 0:
            total += fib_val
        
        fib_index += 1

    return total

print(solution(MAX_VALUE))
