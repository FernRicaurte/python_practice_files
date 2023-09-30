def greeting(name):    # <-- The function definition
    print("Hello", name) # <-- the name parameter is assigned to the passed in value of input_name, which is "Fernando"
# Main program- the program starts running here. This is called the main body of the program.
name1 = input("Enter your name:\n") # <-- The 1st line of code that is not in a function definition is where the program starts.
greeting(name1)
name2 = input("Enter another name:\n")
greeting(name2) # <-- call to the greeting function, the value of name2 is passed in.

# SCOPE

# Local Scope- a variable created (defined) inside of a function can only be used inside that function.
# This means that the variable: name in the above function only exists inside the function (greeting) where it was defined. If we try to print name in the main body of the program we get an error- that name is undefined. 

#Global Scope- a variable created in the main body of the program is a global variable
"""
def greeting():
    print("Hello", name)
# main program
name = input("Enter your name:/n")  # The program using the global name variable works the same as before, but it can get messy bc what if you want another name?
greeting()
"""


# WHY USE A FUNCTION? 
# 1. Because we want to reuse a chunk of code over and over again. We want it in one central location where we can call that function repeatedly.
# 2. Because we want to group our code into logical units
