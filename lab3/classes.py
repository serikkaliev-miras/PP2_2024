# 1
import math


class Myclass:

    def getstring(self):
        self.s = input("")

    def upper(self):
        print(self.s.upper())


result = Myclass()
result.getstring()
result.upper()

# 2


class Shape:
    def area(self):
        self.areaa = 0


class Square(Shape):
    def __init__(self):
        self.a = int(input(""))

    def area(self):
        self.areaa = self.a * self.a
        print(self.areaa)


d = Square()
d.area()

# 3


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

# 4


class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Points at the beginning : {self.x} , {self.y}")

    def move(self, nx, ny):
        self.x = nx
        self.y = ny
        print(f"New ponts : {self.x} , {self.y}")

    def dis(self):
        x2, y2 = int(input("")), int(input(""))
        distance = math.sqrt((x2 - self.x)**2 + (y2 - self.y)**2)
        print(f"Distance between two points : {distance}")


x1, x2 = int(input("")), int(input(""))
result = point(x1, x2)
result.show()
new_x, new_y = int(input("Enter new x: ")), int(input("Enter new y: "))
result.move(new_x, new_y)
result.dis()
