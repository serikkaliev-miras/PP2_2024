from movies import movies

import random

# 1


def func():
    x = random.choice(movies)
    if x["imdb"] > 5.5:
        print(x["name"], True)
    else:
        print(x["name"], False)


print(func())

# 2


def sub():
    for movie in movies:
        if movie["imdb"] > 5.5:
            print(movie["name"])


sub()
