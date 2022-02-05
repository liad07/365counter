from datetime import date
day1=date.today()
day2=date(2021,12,31)

diff=day1-day2
print("today project is",diff.days)