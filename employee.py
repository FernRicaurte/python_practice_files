class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        

class SalaryEmployee(Employee): # I want the new SalaryEmployee to derive from parent Employee class, so I pass it in.
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname) # Within the __init__ method, I can call the parent Employee class __init__ method with super().__init__ and then pass in lname and fname in parentheses.
        self.salary = salary # This property/value is exclusive to the SalaryEmployee class.
        
    def calculate_paycheck(self):
        return self.salary/52