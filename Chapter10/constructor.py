class employee:
    company = "Google"


    def __init__(self, name , salary, subunit):
        self.name = name
        self.salary = salary
        self.subinit = subunit
        print("Employee is created!")
        print("The best programming language is Java")


    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The name of the employee is {self.salary}")
        print(f"The name of the employee is {self.subinit}")

#__init_ is a special type of method in python which intialises the object.

    def getsalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9:00Am in the morning")

harry = employee("rishuu" , 1000 , "Youtube")
harry.getDetails()