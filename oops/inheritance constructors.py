"""inheritance constructors demonstrate how constructors are called in an inheritance hierarchy.
    When a derived class is instantiated, the constructor of the base class is called first, followed by the constructor of the derived class.
    This ensures that the base class is properly initialized before the derived class adds its own initialization."""

class A:
    def __init__(self):
        print("init A ")
    def feature1(self):
        print("feature 1 working")
        
class B:
    
    def __init__(self):
        super().__init__()
        print("In init B")
        
    def feature2(self):
        print("feature 2 working")

class C(A,B):
    def __init__(self):
        super().__init__()
    def feature4(self):
        print("feature 4 working")
        

a = B()
b = C()

