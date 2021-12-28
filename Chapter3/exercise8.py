# Complete the examples in the docstring and then write the body of the following function:

# The Questions
# Q1. What do you name the function?
# Q2. What are the parameters, and what types of information do they refer to?
# Q3. What calculations are you doing with that information?
# Q4. What information does the function return?
# Q5. Does it work like you expect it to?

# Implementation
# 1 Examples and function name
# 2 Header: Decide param names and types, and return type. Write header of the func.
# 3 Description: short description of the function for others to read
# 4 Body: write body of the function
# 5 Test: run examples to make sure you function body is correct

import math

def weeks_elapsed(day1, day2):
    """ (int, int) -> int
    day1 and day2 are days in the same year. Return the number of full weeks
    that have elapsed between the two days.
    >>> weeks_elapsed(3, 20)
    2
    >>> weeks_elapsed(20, 3)
    2
    >>> weeks_elapsed(8, 5)
    0
    >>> weeks_elapsed(40, 61)
    3
    """
    return math.floor(abs(day2 - day1) / 7)
