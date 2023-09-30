class Robot_Dog:
    def __init__(self, name, breed): # The __init__() method lets us initialize our robot's properties.
        self.name = name
        self.breed = breed
    def bark(self): # This is a Class Method for one of the robot dog's behaviors- barking. A Method is a function that belongs to a Class. We create a Class Method just like a function. Except a Method has self as the first parameter.
        print("Woof Woof!") 
# Main Program
my_dog = Robot_Dog("Spot", "Chihuahua")  #Robot_Dog is Name of Class; Inside parentheses--> "Spot"&"Chihuahua" are Property Values--> These are the values for the parameters name_val and breed_val.
print(my_dog.name)
print(my_dog.breed)
my_dog.bark() # We call the bark Method by --> object_name.method_name()


        
    