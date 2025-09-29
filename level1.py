import sys

number1 = []
number2 = []

for fsdfs in sys.stdin:
    if fsdfs.rstrip() == "done":
        thingy = 0
        for i in range(len(number1)):
            print(str(number1[i]) + " " + str(number2[i]))
            thingy += number1[i] * number2[i]
        
        if thingy > 80:
            print("4")
        elif thingy > 70:
            print("3")
        elif thingy > 60:
            print("2")
        elif thingy > 50:
            print("1")
        elif thingy < 50:
            print("fail")

        exit()
        
    number1.append((fsdfs.split()[0]))
    number2.append((fsdfs.split()[1]))

# Why is this a level 1?
# Some regard for the spec, but things are left out. Eg does not say PASS/FAIL seperately, it is bundled in with the grade level. checks for "done" rather than "DONE"
# variables have very obscure names. 
# Logical errors (doesnt divide weight by 100, fails to check for if values are exactly 80, 70, 60, 50)
# Runtime error due to one small mistake (doesn't cast string to integer in the append step)
