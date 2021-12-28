# define a function that:
#  has four parameters, all of them grades between 0 and 100 inclusive, and
#  returns the average of the best 3 of those grades.
# 
#  Hint: Call the function that you defined in the previous exercise.

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
# A   average_best_three()

# Q2. What are the parameters, and what types of information do they refer to?
# A   grade1, grade2, grade3, grade4 represent numbers refering to input grades

# Q3. What calculations are you doing with that information?
# A   calculate bigest three numbers and compute avergage from them
# compute the minimum, sum all four numbers then substract the minimum

# Q4. What information does the function return?
# A   number representing an average

# Q5. Does it work like you expect it to?

def average_best_three(grade1: int, grade2: int, grade3: int, grade4: int) -> int:
    """
    from input of four numbers average biggest three
    average_best_three(1, 10, 20, 30)
    20
    """
    min_grade = min(grade1, grade2, grade3, grade4)
    sum = grade1 + grade2 + grade3 + grade4 - min_grade
    average = sum / 3
    return int(average)