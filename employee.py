class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        

class Salary Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        
    def calculate_paycheck(self):
        return self.salary/52