numheads, numlegs = int(input("")), int(input(""))


def solve(numheads, numlegs):
    # print((numlegs / 2) - numheads, numheads - ((numlegs / 2) - numheads))
    a = (numlegs / 2) - numheads
    b = numheads - ((numlegs / 2) - numheads)
    print(int(a), int(b))


solve(numheads, numlegs)
