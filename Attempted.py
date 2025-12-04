class Attempted:
    def __init__(self, value):
        self.value = value
        
    def sub(self,another):
        return self.value - another.value

a,b = map(int,input().split())

obj1 = Attempted(a)
obj2 = Attempted(b)

print(obj1.sub(obj2))
