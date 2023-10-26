acronym = input("What acronym do you want to add?\n") # Ask the user what acronym they want to add
definition = input("What is the definition?\n")# Then ask the user for the definition
with open("acronyms.txt", "a") as file: # Open the file
    file.write(acronym + " - " + definition + "\n") # Write the new acronym and definition to the file