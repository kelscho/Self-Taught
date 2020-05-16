"""Create a class called Shape. Define a method in it called what_am_i
that prints "I am a shape" when called. Change your Square and Rectangle 
classes from the previous challenges to inherit from Shape, create
Square and Rectangle objects, and call the new method on both of them."""
class Shape():
    def what_am_i(self):
        print("I am a shape.")


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2


class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

a_rectangle = Rectangle(20, 50)
a_square = Square(29)

a_rectangle.what_am_i()
a_square.what_am_i()