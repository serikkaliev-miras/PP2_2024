import datetime
x = datetime.datetime.now()
x_second = x.timestamp()
any = datetime.datetime(2024, 2, 16, 10, 12, 10)
any_second = any.timestamp()
print(abs(x_second - any_second))
