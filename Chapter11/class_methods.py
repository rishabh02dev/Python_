class Employee:
    company = "Camel"
    salary = 100
    location = "Dehli"

    @classmethod
    def changedSalary(cls, sal):
       cls.salary = sal

e = Employee()
print(e.salary)
e.changedSalary(455)
print(e.salary)
print(Employee.salary)