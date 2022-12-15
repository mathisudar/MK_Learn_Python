class MyClass:
  x = 5        # property named x

print(MyClass) # <class '__main__.MyClass'>



class MyClass2:
  x = 5

p1 = MyClass2() #  object named p1
print(p1.x) # 5



class Person:
  def __init__(self, name, age): # built-in __init__() function.
    self.name = name # assign values to object properties
    self.age = age # assign values to object properties

p1 = Person("John", 36)

print(p1.name) # John
print(p1.age) # 36




class Person2:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self): # method in the class:
    print("Hello my name is " + self.name) # Hello my name is John

p1 = Person2("John", 36)
p1.myfunc()


class Person3:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name) # Hello my name is John

p1 = Person3("John", 36)
p1.myfunc()



class Person4:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name) # Hello my name is John

p1 = Person4("John", 36)

p1.age = 40

print(p1.age) # 40



class Person5:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person5("John", 36)

del p1.age

print(p1.age) # AttributeError: 'Person5' object has no attribute 'age'



class Person:
    def __init__(self,age,name):
        self.age = age
        self.name = name
        
    def myFunc(self):
        print("My name is ",self.name,"and my age is",self.age)
        
myObject1 = Person(40, "Mathi")



myObject1.myFunc() # My name is  Mathi and my age is 40
print(myObject1.age) # 40
print(myObject1.name) # Mathi



class Students:
    def __init__(self,studentName,studentClass,studentAge):
        self.studentName = studentName
        self.studentClass = studentClass
        self.studentAge = studentAge
        
    def myFunction(self):
        print("Student",self.studentName,"of class",self.studentClass,"age, is",self.studentAge)
        # Student Shakthi of class 7 age, is 12

myObject1 = Students("Shakthi",7,12)        
 

   
myObject1.myFunction()
print(myObject1.studentName) # Shakthi
print(myObject1.studentClass) # 7
print(myObject1.studentAge) # 12




