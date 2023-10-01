class Robot:
    def __init__(self, name):
        self.name = name
        self.position = [0,0]
        print("My name is", self.name)
        
    def walk(self, x):
        self.position[0] = self.position[0] + x
        print("New position:", self.position)
        
class Robot_Dog(Robot): # The Robot_Dog class will inherit the name, position properties and print out the passed in name, since it did not have its own __init__ method; it will also inherit the walk method that establishes a new position the passed x value. It will, however, have its own make_noise method which prints "Woof woof!"
        def make_noise(self):
            print("Woof Woof!")
            
my_robot_dog = Robot_Dog("Bud")
my_robot_dog.walk(10)
my_robot_dog.make_noise()
        