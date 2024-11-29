""" 
README: Welcome to my calculator project. For any further information please feel free
to reach out to me via Linkedin. Thank you for taking the time to view my project. 

"""

import re

# Title of Calculator 
print("PY Calculator")
print("-------------")

# Setting variables

previous = 0
run = True

# Defining a function 
def performMath():
    global run
    global previous
    if previous == 0:
        equation = input ("Enter your equation: ")
    else:
        equation = input(str(previous))
        
        
    if equation == "quit":
        print("Goodbye, thankyou for using PY Calculator!")
        run = False
    else:
        equation = re.sub('[a-zA-Z,:()+""]','',equation)
        
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous)) + equation
        print(f"You have typed {previous}")
        
        
# Putting a loop to continously run as long as everything is true 
while run:
    performMath()