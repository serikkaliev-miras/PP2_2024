from movies import movies

import random


def func():
    x = random.choice(movies)
    if x["imdb"] > 5.5:
        print(x["name"], True)
    else:
        print(x["name"], False)


print(func())
