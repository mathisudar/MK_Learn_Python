class AreaCircleClass:
    def AreaCircleMethod(circleRad):
        PI = 3.14159
        areaCircleOut = PI * circleRad * circleRad
        return areaCircleOut

# Driver Code

print('Area of circle1:',AreaCircleClass.AreaCircleMethod(10))
print('Areaof circle2:',AreaCircleClass.AreaCircleMethod(100))
