def unique(listt):
    newlistt = []
    for element in listt:
        if element not in newlistt:
            newlistt.append(element)
    return newlistt


numbers = input("")
l = list(map(int, numbers.split()))
result = unique(l)
print(result)
