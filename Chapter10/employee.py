class Employee:
    company = "Google"
    salary = 5000

harry = Employee()
rajni = Employee()
harry.salary = 300
rajni.salary = 400

print(harry.company)
print(rajni.company)
Employee.company = "Twitter"
print(harry.company)
print(harry.salary)
print(rajni.salary)


#Instance attributes that belongs to the instances(object)partcular instance like rohit's adhaar number or his salary assuming the class from the previous example. and other is class attributes.