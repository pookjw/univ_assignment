from math import pi

class Geometric_item:
    counter = 0
    def __init__(self, color):
        self.color = color
        Geometric_item.counter += 1

class Rectangle(Geometric_item):
    def __init__(self, color, length, breadth):
        super().__init__(color)
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length*self.breadth
    def information(self):
        print(self.color, self.length, self.breadth, self.area())

class Circle(Geometric_item):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    def area(self):
        return self.radius*self.radius*pi
    def information(self):
        print(self.color, self.radius, self.area())

rectangle = Rectangle("yellow", 4, 4)
print(rectangle.area())
rectangle.information()

circle = Circle("Blue", 3)
print(circle.area())
circle.information()

print(Geometric_item.counter)
