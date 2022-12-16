"""
What should happen when calling + on multiple 'objects'
    TypeError: unsupported operand type(s) for +

To define what happens when adding objects, 
you need to implement the __add__() method in the class.


@author: Mathi Krishnan

"""

class Weights:
    def __init__(self,baseWeight):  
        self.baseWeight = baseWeight

    def __add__(self,otherWeights): # Operator overloading (Addition)
        return Weights(self.baseWeight + otherWeights.baseWeight)
    
        
weightObj1 = Weights(50)  # Objects
weightObj2 = Weights(150)
weightObj3 = Weights(100)

totalWeight = weightObj1 + weightObj2 + weightObj3 # addition of objects


print("Total Weight:",totalWeight.baseWeight)



'''
    Result: Total Weight: 300
'''
     
