import datetime
import random

try:
    date1 = datetime.datetime(*list(map(int, input("--Enter the first date--\n>> ").split('-')))[:3])
    date2 = datetime.datetime(*list(map(int, input("--Enter the second date--\n>> ").split('-')))[:3])
    random_date = date1 + (date2 - date1) * random.random()
    print(f"first date: {date1.date()}")
    print(f"second date: {date2.date()}")
    print(f"the random date: {random_date.date()}")
    if random_date.weekday() == 0:
        print("אין לי ויניגרט!")
except TypeError:
    print("Invalid input")
except ValueError:
    print("Invalid date")
