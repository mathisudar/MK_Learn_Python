"""
In Python, double-underscore methods (also known as dunder methods) 
make operator overloading possible.

A common example of a dunder method is the __init__ method. 
This method is automatically called when an object is created.

"""

# Double Underscore Methods in Python
       
class Fruits:
    def __init__(self,nameFruit):
        self.nameFruit = nameFruit
        
appleFruit = Fruits("Apple") # Object 

print("Name of the Fruit:",appleFruit.nameFruit)

 

''' Result:
        Name of the Fruit: Apple 
        
        '''
        
