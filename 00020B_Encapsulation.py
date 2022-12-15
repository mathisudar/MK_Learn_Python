class Company: # Base class
    def __init__(self):
        self._project = "NLP" # Protected Member
        
class Employee(Company): # Child class
    def __init__(self,name):
        self.name = name
        Company.__init__(self)
        
    def show(self):
        print("Employee Name:",self.name)
        print("Working Project:",self._project) # protected member inside the Method
        
        
employeeObj1 = Employee("Mathi")  

employeeObj1.show()
print(employeeObj1._project)


*** Result ***

Employee Name: Mathi
Working Project: NLP
NLP

*** Result ***
