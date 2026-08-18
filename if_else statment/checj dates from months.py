# import calendar
# import random
# month=[random.randint(1,12) for _ in range(12)]
# month.sort()
# calendar.
import calendar

year = 2019
obj = calendar.Calendar()

for month in range(1,13):
  
  day_count = 0

# iterating with itermonthdays
  for day in obj.itermonthdays(year, month):
    if day!=0:
     
     day_count+=1
  print(f"Month {month}: {day_count} days total")  