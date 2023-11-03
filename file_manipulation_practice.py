import os # We need to import the os module to be able to use its functions (make directories, list files, and move files)
# os.mkdir("/User/fernsmachine/Desktop/CleanedUp") <-- making a directory(folder) on the Desktop
folder = "/Users/fernsmachine/Desktop/"
entries = os.scandir(folder)
for entry in entries:
    if os.path.isfile(entry):
        print("File:", entry.name)
    elif os.path.isdir(entry):
        print("Directory:", entry.name)
