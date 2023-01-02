class employee:
    company = "Google"
    def getsalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")


harry = employee()
harry.salary = 10000
harry.getsalary()
#this harry.getsalary() can be simplified as employee.getsalary(harry)