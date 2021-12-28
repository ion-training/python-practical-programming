# complete the examples in doc stings and write the body of the function

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

def total_length(s1: str, s2: str) -> int:
    """ Return the sum of the lengths of s1 and s2.
    >>> total_length('yes', 'no')
    5
    >>> total_length('yes', '')
    3
    >>> total_length('YES!!!!', 'Noooooo')
    14
    """
    return len(s1+s2)