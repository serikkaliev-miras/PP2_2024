from movies import movies


# 1


def func(m):
    x = input("")
    for i in m:
        if i["name"] == x and i["imdb"] > 5.5:
            print(True)


func(movies)


# 2
mylist = []


def sub():
    for movie in range(len(movies)):
        if movie["imdb"] > 5.5:
            mylist.append(movie["name"])
    return mylist


print(sub())

# 3
c = input("")


def cat(c):
    for i in movies:
        if i["category"] == c:
            print(i["name"])


cat(c)

# 4


def average():
    total = 0
    inp = input("")
    films = [x.strip() for x in inp.split(',')]
    for movie in movies:
        if movie["name"] in films:
            total += movie["imdb"]
    return total / len(films)


print(average())
