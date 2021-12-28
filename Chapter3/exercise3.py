# define a function that:
#  has one parameter, a number, and returns that number tripled.

# Q1: What do you name the function?
# A: number_tripled

# Q2: What are the parameters, and what types of information do they refer to?
# A: one parameter of type number

# Q2: What calculations are you doing with that information?
# A: the input number (parameter) is going to be multiplied 3 times

# Q3: What information does the function return?
# A: The function returns the result of the input trippled input parameter

# 1 Examples
# 2 Header: Decide param names and types, and return type. Write header of the func.
# 3 Description: short description of the function for others to read
# 4 Body: write body of the function
# 5 Test: run examples to make sure you function body is correct

def number_tripled(num: int) -> int:
    """
    precondition: number is a number
    take as input a number and multiply the number 3 times
    
    >>> number_tripled(5)
    125

    >>> number_tripled(2.2)
    6
    """
    return num*3




# Q: Does it work like you expect it to?
# A:


