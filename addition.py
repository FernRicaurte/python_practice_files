def addition(a, b):  # Define the function
    return a+ b

# Main program:
def main(): # <-- Now all of the program is contained inside the this main() function.
    num1 = float(input("Enter your 1st number\n"))  # <-- The main program starts running here
    num2 = float(input("Enter your 2nd number\n"))

# Calling our function:
    result = addition(num1, num2)
    print("The result is", result)

main() # We need to call main() after the functions are declared.