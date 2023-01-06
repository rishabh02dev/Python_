class Employee:
    company = "Bharat Gas"
    salary = 1000
    salarybonus = 1000
    # totalSalary  = salary + salarybonus
 
    @property #this is a setter method
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter
    def totalSalary(self , val):
        self.salarybonus = val - self.salary

e = Employee()
print(e.totalSalary)
e.totalSalary = 5800
#this is a getter method.
print(e.salary)
print(e.salarybonus)
