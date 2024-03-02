tuuple = tuple(map(str, input().split()))


def f(tuuple):
    cnt = 0
    for i in tuuple:
        if i == "True":
            cnt += 1
    if cnt == len(tuuple):
        return True
    return False


if f(tuuple):
    print("True")
else:
    print("False")
