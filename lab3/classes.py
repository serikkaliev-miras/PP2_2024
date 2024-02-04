# 1
class Myclass:
    def __init__(self):
        self.string = ''

    def getstring(self):
        self.string = input("")

    def upper(self):
        print(self.string.upper())


result = Myclass()
result.getstring()
result.upper()
