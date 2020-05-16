"""Define a method in your Square class called change_size that
allows you to pass in a number that increases or decreases
(if the number is a negative) each side of a Square object by that
number."""
class Square():
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

    def change_size(self, new_size):
        self.s1 += new_size

a_square = Square(100)
print(a_square.s1)

a_square.change_size(200)
print(a_square.s1)