# Problem 4: Largest Palindrome Product

## Problem Statement

A palindromic number reads the same both ways. The largest palindrome made from the product of two $3$-digit numbers is $906609 = 913 \times 993$.

Find the largest palindrome made from the product of two $3$-digit numbers.

## Solution

The solution to this problem is implemented in the `solution.py` file. The program defines a function `is_palindrome` to check if a given string is a palindrome. Additionally, there is a function `is_product_of_two_n_digit` that checks if a number is a product of two $n$-digit numbers. The main function `solution` iterates through possible palindrome numbers in descending order and checks if they are products of two $3$-digit numbers. The result, the largest palindrome made from the product of two $3$-digit numbers, is printed to the console.

### How it Works

1. The `is_palindrome` function checks whether a given string is a palindrome by comparing it to its reverse.

2. The `is_product_of_two_n_digit` function checks if a given number is a product of two $n$-digit numbers. It iterates through possible divisors to find a pair of $n$-digit numbers whose product is the given number.

3. The `solution` function finds the largest palindrome number that is a product of two $3$-digit numbers. It iterates through possible palindrome numbers in descending order and checks if they satisfy the conditions using the `is_palindrome` and `is_product_of_two_n_digit` functions.

## How to Run

To execute the solution, run the following command:

```bash
python solution.py
