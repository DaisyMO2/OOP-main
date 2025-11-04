class Shape:
    def __init__(self, area):
        area = area
        
class rectangle(Shape):
    def __init__(self, l, w):
        self.l = 8
        self.w = 4
        print("l * w")
        
class circle(Shape):
    def __init__(self, r, pi):
        self.r = 5
        self.pi = 3.14
        print("pi * r^2")
        
items = [rectangle(8*4), circle(5*3.14)]
for item in items:
    print(item)

        