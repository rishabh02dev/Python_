class Person:

    country = "India"
    def __init__(self):
        print("Intializing Person...\n")
    def takeBreath(self):
        print("I am breathing...")
 
class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()
        print("Intialazing Employee...")
    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so I am luckily breathing")

class Programmer(Employee):
    company = "Fiverr"

    def __init__(self):
        super().__init__()
        print("Intialazing Programmer...\n")

    def getSalary(self):
        print(f"No salary to programmers")

    def takeBreath(self):
        super().takeBreath()
        print("I am a programmer so I am breathing++...")

# p = Person()
# p.takeBreath()
#print (p.company) will throw an error

# e = Employee()
# e.takeBreath()


pr = Programmer()
pr.takeBreath()

