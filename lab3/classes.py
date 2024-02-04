# 1
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
