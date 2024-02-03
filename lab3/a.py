from movies import movies

c = input("")


def cat(c):
    for i in movies:
        if i["category"] == c:
            print(i["name"])


cat(c)
