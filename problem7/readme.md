# Problem 7: 10,001st Prime

## Problem Statement

By listing the first six prime numbers: $2, 3, 5, 7, 11$, and $13$, we can see that the $6th$ prime is $13$.

What is the $10,001st$ prime number?

## Solution

The solution to this problem is implemented in the `solution.py` file. The program defines two functions:

1. `is_prime_number`: Checks if a given number is prime. Excluding even numbers before entering the loop can result in more efficient checking. Note that we are only checking odd numbers inside the loop by using 2 as the increasing step value.

    ```python
    def is_prime_number(number):
        """
        Check if a number is prime.

        Args:
            number (int): The number to check for primality.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if number < 2 or number % 2 == 0:
            return False
        if number == 2:
            return True

        sqrt = math.isqrt(number)
        return all(number % div != 0 for div in range(3, sqrt + 1, 2))
    ```

2. `solution`: Finds the nth prime number.

    ```python
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
    ```

The solution is executed for the $10,001st$ prime number, and the result is printed to the console.

### How it Works

1. The `is_prime_number` function checks if a given number is prime by excluding even numbers and only checking odd numbers inside the loop.

2. The `solution` function iterates through numbers and checks for primality using the `is_prime_number` function until it finds the $n$th prime number.

3. The result, the $10,001st$ prime number, is printed to the console.

## How to Run

To execute the solution, run the following command:

```bash
python solution.py
