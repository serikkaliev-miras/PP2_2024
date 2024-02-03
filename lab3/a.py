from movies import movies


def summ():
    cnt = 0
    for movie in movies:
        cnt = cnt + movie["imdb"]
    print(cnt)


summ()
