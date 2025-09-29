import sys

grade = []
weight = []

for line in sys.stdin:
    if line.rstrip() == "done":
        g = 0
        for i in range(len(grade)):
            print(str(grade[i]) + "%\t" + str(weight[i]) + "%")
            g += grade[i] * (weight[i])
        
        if g > 80:
            print("4")
        elif g > 70:
            print("3")
        elif g > 60:
            print("2")
        elif g > 50:
            print("1")
        elif g < 50:
            print("R")

        if g > 50:
            print("PASS")
        elif g < 50:
            print("FAIL")
            
        exit()
        
    grade.append(int(line.split()[0]))
    weight.append(int(line.split()[1]))

# Why is this a level 2?
# Doesn't match the spec ("done" instead of "DONE")
# Table lacks clear communication (levels just say "4", "3")
# Poor organization. No comments. Doesn't use functions. Variable names are not very helpful
# More serious logical flaws (Doesn't consider the case where the grade is exactly 50, which makes it not output part of the answer in that case). weight is not divided by 100
# code is not organized into functions