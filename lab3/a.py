from movies import movies


def average():
    total = 0
    inp = input("")
    films = [x.strip() for x in inp.split(',')]
    for movie in movies:
        if movie["name"] in films:
            total += movie["imdb"]
    return total / len(films)


print(average())
