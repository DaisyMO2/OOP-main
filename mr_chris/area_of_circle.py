#area of a circle
class circle:
   def __init__(self, radius):
    self.radius = radius
   
   def area (self):
       return 3.14 * self.radius * self.radius
   

#creation of objects
c1 = circle (8)
c2 = circle(6.5)

print (f"the area of the circle c1 is", c1.area())
   
   