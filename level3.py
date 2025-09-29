import sys

def calculate_grade(grades, weights):
    print("ASSIGNMENT\tGRADE\tWEIGHT")
    grade = 0
    for i in range(len(grades)):
        print("Assignment " + str(i) + ":\t" + str(grades[i]) + "%\t" + str(weights[i]) + "%")
        grade += grades[i] * (weights[i] / 100)
    
    print("\nFinal grade : " + str(grade))
    
    # If grade is over 80
    if grade > 80:
        print("Level 4")
    # If grade is over 70
    elif grade > 70:
        print("Level 3")
    # If grade is over 60
    elif grade > 60:
        print("Level 2")
    # If grade is over 50
    elif grade > 50:
        print("Level 1")
    # If grade is less than 50
    else:
        print("Level R")

    if grade > 50:
        print("PASS")
    else:
        print("FAIL")
        

# Make the grades and weights lists
grades = []
weights = []

# Loop until the user types DONE
for line in sys.stdin:
    if line.rstrip() == "DONE":
        calculate_grade(grades, weights)
        exit()
    
    l = line.split()
    grade = int(l[0]) # Take the first number and store it in "grade"
    weight = int(l[1]) # Take the second number and store it in "weight"

    # add those numbers into both the lists
    grades.append(grade)
    weights.append(weight)



# What makes this a level 3?
# Substantially matches the expectation
# No "extras"
# Minor logical flaws 
#   - Grade checks use > instead of >=
# Uses comments, but lacking some effectiveness (over commenting)
# Good variable and function names.