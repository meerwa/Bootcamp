import math

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius
    
    def compute_perimeter(self):
        return 2 * math.pi * self.radius
    
    def compute_area(self):
        return math.pi * (self.radius ** 2)
    
    def print_definition(self):
        print("A circle is a shape with all points equidistant from its center.")


circle = Circle(5)
print("Perimeter:", circle.compute_perimeter())
print("Area:", circle.compute_area())
circle.print_definition()
