import datetime
x = datetime.datetime.now()
print(int(x.strftime("%d")) - 5)

# x = datetime.datetime.now()
# print(f"{x.year}-{x.month}-{x.day-5} {x.hour}:{x.minute}:{x.second}")
