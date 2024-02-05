import math 

class Point(): 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
    def show(self): 
        return self.x , self.y
    def move(self,x1,y1): 
        self.x += x1 
        self.y += y1 
    def dist(self,x2,y2):
        d = math.sqrt((self.x - x2)**2 + (self.y - y2)**2)
        return d 

x,y = map(int, input().split())
p1 = Point(x,y) 
print(p1.show()) 

x1,y1 = map(int, input().split())
p1.move(x1,y1)
print(p1.show())

x2 = x
y2 = y
d = p1.dist(x2,y2) 
print(d)

