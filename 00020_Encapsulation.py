class EmployeeDetails:
    def __init__(self,name,age,gender,salary):
        self.name = name # public
        self.__age = age # private
        self.gender = gender # public
        self.__salary = salary # private
        
        
    def get_age(self): # for retrieve the data
       return self.__age
   
    def set_age(self,age): # for modify the data
        self.__age = age
        
        
    def get_salary(self):# for retrieve the data
        return self.__salary

        
employee1 = EmployeeDetails("Mathi", 43, "M", 1e5)

employee1.set_age(45)

print("Name:",employee1.name)
print("Age:",employee1.get_age())
print("Gender:",employee1.gender)
print("Salary:",employee1.get_salary())


# Another method to call the private member variable
print("Age:",employee1._EmployeeDetails__age) # object._className__variableName



*** Result ****

Name: Mathi
Age: 45
Gender: M
Salary: 100000.0
Age: 45  
*** Result ****  
  
