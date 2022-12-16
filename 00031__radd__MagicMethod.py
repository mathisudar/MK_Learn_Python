"""
Adding Different Types of Objects Together


#1 totalWeight = weightObj1 + 300 # addition of 'object with int'
     TypeError: unsupported operand type(s) for +: 'Weight' and 'int' 


#2 totalWeight =  300 + weightObj1 # addition of int with object
    TypeError: unsupported operand type(s) for +: 'int' and 'Weight'

The Python __radd__() method implements the reverse addition operation 
that is addition with reflected, swapped operands. 


So, when you call x + y, Python attempts to call x.__add__(y). 
Only if the method is not implemented on the left operand, 
Python attempts to call __radd__ on the right operand.


And if this isn’t implemented either, it raises a TypeError.

    
@author: Mathi Krishnan

"""

class Weights:
    def __init__(self,baseWeight):  
        self.baseWeight = baseWeight
        
    def __add__(self,otherWeights): # Operator overloading (Addition)
       if type(otherWeights == int):
           return Weights(self.baseWeight + otherWeights)
       else:
           return Weights(self.baseWeight + otherWeights.baseWeight)  

    def __radd__(self,otherWeights): # Operator overloading (Reverse Addition)
       if type(otherWeights == int):
           return Weights(self.baseWeight + otherWeights)
       else:
           return Weights(self.baseWeight + otherWeights.baseWeight)
    
        
weightObj1 = Weights(50)  # Objects

totalWeight1 = weightObj1 + 300 # addition of ' object with int'
totalWeight2 = 300 + weightObj1 # Reverse addition of 'int with object'


print("Total Weight:",totalWeight1.baseWeight)
print("Total Weight:",totalWeight2.baseWeight)


'''
    Result: 
        Total Weight: 350
        Total Weight: 350
'''
