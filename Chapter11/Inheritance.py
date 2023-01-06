class Employee:
    company = "Google"

    def showDetails(self):
        print("This is is an employee")
 
class programmer(Employee):
    language = "Python"
    company = "Youtube"

    def getLanguage(self):
        print(f"The language is{self.language}")
 
    def showDetails(self):
        print("This is an employee")




e = Employee()
e.showDetails()
p = programmer()
p.showDetails()
p.getLanguage()
print(p.company)
