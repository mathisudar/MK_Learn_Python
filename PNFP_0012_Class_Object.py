class Represent(object):
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __repr__(self):
        return "Represent(x={},y=\"{}\")".format(self.x, self.y)
    def __str__(self):
        return "Representing x as {} and y as {}".format(self.x, self.y)
        
r = Represent(1, "Hopper") # Object

rep = r.__repr__()
print(rep)

myStr = r.__str__()
print(myStr)


"""

Output
Represent(x=1,y="Hopper")
Representing x as 1 and y as Hopper

"""
