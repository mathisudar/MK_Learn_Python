class Shape:
    def __init__(self,side1,side2,side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        
class Rectangle(Shape):
    def __init__(self,side1,side2,side3):
        Shape.__init__(self,side1,side2,side3)
        
    def displayArea(self):
        print("Area of Rectangle:",self.side1*self.side2)
        

class Square(Shape):
    def __init__(self,side1,side2,side3):
        Shape.__init__(self,side1,side2,side3)
        
    def displayArea(self):
        print("Area of Square:",self.side1 * self.side1)
        
    
objRec = Rectangle(100,200,300)
objRec.displayArea()

objSq = Square(100,200,300)
objSq.displayArea()
