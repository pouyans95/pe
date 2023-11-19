# Problem 6: Sum Square Difference

## Problem Statement

The sum of the squares of the first ten natural numbers is,

$$1^2 + 2^2 + ... + 10^2 = 385.$$

The square of the sum of the first ten natural numbers is,

$$(1 + 2 + ... + 10)^2 = 55^2 = 3025.$$

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

## Solution

The solution to this problem is implemented in the `solution.py` file. The program defines a function `solution` that calculates the difference between the square of the sum and the sum of the squares of numbers from 1 to the given upper limit.

### Args
- `upper_limit_num` (int): The upper limit of the range of numbers.

### Returns
- int: The difference between the square of the sum and the sum of the squares.

### Example
```python
>>> solution(10)
2640

How it Works
The function calculates the sum of squares using a generator expression for numbers from 1 to the given upper limit.

The square of the sum is calculated using the built-in sum function for the range from 1 to the given upper limit.

The difference between the square of the sum and the sum of squares is returned.

The solution for the first one hundred natural numbers is obtained by calling the function with the argument 100.

## How to Run

To execute the solution, run the following command:

```bash
python solution.py
