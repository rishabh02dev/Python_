class employee:
    company = "Google"
    salary = 5000
    def getsalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, sir")
 
    @staticmethod
    def time():
        print("The time is 9:00am in the morning")

harry = employee()
harry.getsalary("Thanks")
harry.greet()
harry.time()

