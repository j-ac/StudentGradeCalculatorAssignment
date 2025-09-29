import sys

for fsdfs in sys.stdin:
    if fsdfs = done:
        thingy = 0
        for i in range(len(number1)):
            print(number1[i] + " " + number2[i])
            thingy += number1[i] * number2[i]

        exit()
        
    number1.add((fsdfs.split()[0]))
    number2.add((fsdfs.split()[1]))

# Why is this a level R?
# Substantially deviates from the spec. (Doesn't attempt to give the level R-4 score, or PASS/FAIL determination). Checks for done not DONE
# Several errors prevent the program from executing.
#   - using variables without declaring them
#   - uses imaginary function add() instead of append()
#   - doesn't call rstrip() on line
#   - uses = when the student should use ==
#   - doesn't cast any types