"""
What should happen when calling + on multiple 'objects'
    TypeError: unsupported operand type(s) for +

To define what happens when adding objects, 
you need to implement the __add__() method in the class.



# Over Loading ---> SUM of List objects

Without __radd__() this(sum) would not be possible. 
This is because the built-in sum() function starts summing from 0. 

This means the first operation would be (0).__add__(weightObj1), 
which would not work without the reverse add implementation.


@author: Mathi Krishnan

"""
class Weights:
    def __init__(self,baseWeight):  
        self.baseWeight = baseWeight

    def __add__(self,otherWeights): # Operator overloading (Addition)
        if type(otherWeights) == int:
            return Weights(self.baseWeight + otherWeights)
        else:
            return Weights(self.baseWeight + otherWeights.baseWeight)
        
    def __radd__(self,otherWeights): # Operator overloading (Reverse Addition)
        return self.__add__(otherWeights)
        
weightObj1 = Weights(50)  # Objects
weightObj2 = Weights(150)
weightObj3 = Weights(100)

totalWeight = sum([weightObj1, weightObj2, weightObj3]) 
# addition of objects using List


print("Total Weight:",totalWeight.baseWeight)

 
'''
    Result: Total Weight: 300
'''
