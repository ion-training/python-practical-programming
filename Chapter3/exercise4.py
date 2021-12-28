# define a function that:
#  has two parameters, both of which are numbers,
#  and returns the absolute value of the difference of the two.
#  Hint: Call built-in function abs.


# The Questions
# Q1. What do you name the function?
# Q2. What are the parameters, and what types of information do they refer to?
# Q3. What calculations are you doing with that information?
# Q4. What information does the function return?
# Q5. Does it work like you expect it to?


# Q1: What do you name the function?
# A:  abs_of_difference

# Q2: What are the parameters, and what types of information do they refer to?
# A   parameters are 2 arbitrary numbers revered by num1 and num2

# Q3. What calculations are you doing with that information?
# A   compute difference num1 - num2, take the result and compute the absolute value

# Q4. What information does the function return?
# A   a number

# 5. Does it work like you expect it to?


# Implementation
# 1 Examples and function name
# 2 Header: Decide param names and types, and return type. Write header of the func.
# 3 Description: short description of the function for others to read
# 4 Body: write body of the function
# 5 Test: run examples to make sure you function body is correct

def abs_of_difference(num1: int, num2: int) -> int:
    """
    precondition: parameters must be numbers
    calculate difference between num1 and num2 and compute absolute value of the result

    >>> abs_of_difference(-4,5)
    9
    >>> abs_of_difference(1,-3)
    4
    >>> abs_of_difference(2,2)
    0
    """
    return abs(num1 - num2)