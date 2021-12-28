# complete the function from docstrings

# def repeat(s: str, n: int) -> str:
# """ Return s repeated n times; if n is negative, return the empty string.
#         >>> repeat('yes', 4)
#         'yesyesyesyes'
#         >>> repeat('no', 0)
#         >>> repeat('no', -2)
#         >>> repeat('yesnomaybe', 3)
#         """

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

def repeat(s: str, n: int) -> str:
    """ Return s repeated n times; if n is negative, return the empty string.
    >>> repeat('yes', 4)
    'yesyesyesyes'
    >>> repeat('no', 0)
    >>> repeat('no', -2)
    >>> repeat('yesnomaybe', 3)
    """
    if n < 0: return print('')
    print(s*n)