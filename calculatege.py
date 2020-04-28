import calendar
from datetime import datetime, date

print("Your date of birth (mm dd yyyy)")
date_of_birth = datetime.strptime(input("--->"), "%m %d %Y")

today = date.today()
years = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))

if today.month < date_of_birth.month:
    months =  12 - date_of_birth.month + today.month
else:
    months = today.month - date_of_birth.month

if today.day < date_of_birth.day:
    lastmonth = today.month -1
    numberofdaysinlastmonth = calendar.monthrange(today.year, lastmonth)[1]
    days = numberofdaysinlastmonth - date_of_birth.day + today.day
else:
    days = today.day - date_of_birth.day

print("You are {0} years, {1} months, and {2} days old".format(years, months, days))

