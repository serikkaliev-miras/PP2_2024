import datetime
x = datetime.datetime.now()
# 1

yesterday = (x - datetime.timedelta(days=1)).strftime("%A")
tomorrow = (x + datetime.timedelta(days=1)).strftime("%A")
print(yesterday, x.strftime("%A"), tomorrow)

# 2

weekdays = {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "Sunday": 7
}
yesterday = int(x.strftime("%w")) - 1
tomorrow = int(x.strftime("%w")) + 1
for day, number in weekdays.items():
    if yesterday == number:
        print(f"{day}")
print(x.strftime("%A"))
for day, number in weekdays.items():
    if tomorrow == number:
        print(f"{day}")
