class Shape:
    def area(self):
        self.a = 0


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        self.a = self.width * self.length
        print(self.a)


r = Rectangle(int(input("Enter length: ")), int(input("Enter width: ")))
r.area()
