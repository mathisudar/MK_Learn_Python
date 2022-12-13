class Dad():
    def working(self):
        print("Child's dad is working")
        
class Mom():
    def cooking(self):
        print("Child's mom is cooking")
        
class Child(Dad,Mom):
    def playing(self):
        print("Child is playing")
        
childObject = Child()

childObject.working()
childObject.cooking()
childObject.playing()
