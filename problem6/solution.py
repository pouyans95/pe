def solution(upper_limit_num):
    '''## Summary
    Calculate the difference between the square of the sum and the sum of the squares of numbers from 1 to the given upper limit.

    ## Args
    - `upper_limit_num` (int): The upper limit of the range of numbers.

    ## Returns
    - int: The difference between the square of the sum and the sum of the squares.

    ## Examples
    ```python
    >>> solution(10)
    2640
    '''
    sum_of_squares = sum(num**2 for num in range(1, upper_limit_num+1))
    square_of_sum = sum(range(1, upper_limit_num+1))**2
    return square_of_sum - sum_of_squares

print(solution(100))