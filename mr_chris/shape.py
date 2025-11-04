class Shape:
    def __init__(self, area):
        self.area = area

class Rectangle(Shape):
    def __init__(self, l, w):
        area = l * w
        super().__init__(area)
        print(area)

class Circle(Shape):
    def __init__(self, r, pi=3.14):
        area = pi * (r ** 2)
        super().__init__(area)
        print(area)

items = [Rectangle(8, 4), Circle(5)]
for item in items:
    print(item.area)
