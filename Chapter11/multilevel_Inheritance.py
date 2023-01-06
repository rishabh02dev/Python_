class Person:
    country = "India"

    def takeBreak(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreak(self):
        print("I am an Employee so I am luckily breathing...")

class Programmer(Employee):
    company = "Fiverr"

    def getsalary(self):
        print("No salary to programmers")

    def takeBreak(self):
        print("I am a programmer so I am breathing ++")

p = Person()
e = Employee()
pr = Programmer()
e.takeBreak()
p.takeBreak()
print(p.country)
print(e.company)
print(p.country)
print(pr.company)
pr.takeBreak()