# define a function that:
#  has one parameter, a distance in kilometers, and
#  returns the distance in miles. (There are 1.6 kilometers per mile.)


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
# A   miles_to_kilometers

# Q2. What are the parameters, and what types of information do they refer to?
# A   input parameter is miles, refers to a number representing miles

# Q3. What calculations are you doing with that information?
# A   input parameter is multiplied by 1.6 which results in number of kilometers

# Q4. What information does the function return?
#A    returns a number which represents kilometers

# Q5. Does it work like you expect it to?



def miles_to_kilometers(miles: float) -> float:
    """
    take miles input and covert to kilometers by multiplying with 1.6

    >>> miles_to_kilometers(2)
    3.2
    >>> miles_to_kilometers(10)
    16.0
    """
    return miles * 1.6
