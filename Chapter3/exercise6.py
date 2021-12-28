# define a function that:
#  has three parameters, grades between 0 and 100 inclusive, and 
#  returns the average of those grades.

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

# The Questions
# Q1. What do you name the function?
# A.  average_three_numbers

# Q2. What are the parameters, and what types of information do they refer to?
# A.  grade1, grade2, grade3 input parameters that represent numbers from 0 to 100.

# Q3. What calculations are you doing with that information?
# A.  average of grade1, grade2, grade3

# Q4. What information does the function return?
# A.  return average number transformed into an int

# Q5. Does it work like you expect it to?

def average_three_numbers(grade1: int, grade2: int, grade3: int) -> int:
    """
    compute average of 3 input numbers
    >>> average_three_numbers(10, 20, 30)
    20
    """
    average = (grade1 + grade2 + grade3) / 3
    return int(average)
