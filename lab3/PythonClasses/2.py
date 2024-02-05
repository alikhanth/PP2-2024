class Shape(): 
    def __init__(self):
        pass 
    def area(self): 
        return 0 
class Square(Shape):
    def __init__(self,length=0): 
        Shape.__init__(self) 
        self.length = length 
    def area(self): 
        return self.length*self.length
    
a = int(input()) 
s = Square(a)
print(s.area()) 
print(Square().area()) 
