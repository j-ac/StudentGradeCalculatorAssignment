import sys

# Using a list of grades and their matching weights, display them in a table
# Display the final grade on a level R-4 and whether the student passes.
def print_grade_table(grades, weights):
    print("┏━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━┓")
    print("┃ASSIGNMENT   ┃ GRADE  ┃ WEIGHT  ┃")
    print("┣━━━━━━━━━━━━━╋━━━━━━━━╋━━━━━━━━━┫")
    grade = 0
    for i in range(len(grades)):
        # Print numbers with extra padding so that numbers that are bigger/smaller don't ruin spacing
        print(f"┃Assignment {i:<2}┃\t{grades[i]:>3}%   ┃  {weights[i]:>3}%   ┃") 
        grade += grades[i] * (weights[i] / 100)
    
    print("┗━━━━━━━━━━━━━┻━━━━━━━━┻━━━━━━━━━┛")
    print("\nFinal grade : " + str(grade))
    
    if grade >= 80:
        print("Level: 4")
    elif grade >= 70:
        print("Level: 3")
    elif grade >= 60:
        print("Level: 2")
    elif grade >= 50:
        print("Level: 1")
    else:
        print("Level: R")

    if grade >= 50:
        print("PASS")
    else:
        print("FAIL")
        

# Starting point of the program
grades = []
weights = []

print("Please enter your grades per line as <GRADE> <WEIGHT>")
for line in sys.stdin:
    if line.rstrip() == "DONE":
        if sum(weights) > 100:
            print("Error! Weights add up to over 100%")
            exit()

        print_grade_table(grades, weights)
        exit()
    
    # Turn the user's text input into two numbers
    l = line.split()
    grade = int(l[0])
    weight = int(l[1])

    grades.append(grade)
    weights.append(weight)


# What makes this a level 4?
# The algorithm works 100% correctly
# Effective variable/function names
# Effective comments (has comments, but they are not obvious and redundant)
# The student improved upon the basic requirements with a few innovations
#   - Table has a frame
#   - Checks if weights add up to over 100%
#   - Prompts the user with an explanation of how to use the program