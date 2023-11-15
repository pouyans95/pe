# Problem 5: Smallest Evenly Divisible Number

## Problem Statement

$2520$ is the smallest number that can be divided by each of the numbers from $1$ to $10$ without any remainder.

What is the smallest positive number that is **evenly divisible** by all of the numbers from $1$ to $20$?

## Solution

The solution to this problem is implemented in the `solution.py` file. The program defines two functions: `get_gcd` (Greatest Common Divisor) and `get_lcm` (Least Common Multiple). The main function `solution` calculates the smallest positive number that is evenly divisible by all numbers from $1$ to $20$. The solution is obtained by iteratively finding the LCM of the current LCM and the next number in the range.

### Note

Although using the `math` library would improve code speed and performance, for educational reasons, the solution provided manually calculates the GCD and LCM.

### How it Works

1. The `get_gcd` function calculates the Greatest Common Divisor (GCD) of two numbers using the Euclidean algorithm.

2. The `get_lcm` function calculates the Least Common Multiple (LCM) of two numbers using the formula `(num1 * num2) // get_gcd(num1, num2)`.

3. The `solution` function initializes the LCM to $2$ and iterates through the range from $3$ to $20$, updating the LCM at each step.

4. The result, the smallest positive number that is evenly divisible by all numbers from $1$ to $20$, is printed to the console.

## How to Run

To execute the solution, run the following command:

```bash
python solution.py
