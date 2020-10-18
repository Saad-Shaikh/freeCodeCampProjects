def add_time(start, duration, day=None):
  new_time = ""
  days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
  start_time = start.split(" ")[0]
  start_hours = int(start_time.split(":")[0])
  start_minutes = int(start_time.split(":")[1])
  AM_PM = start.split(" ")[1]
  # 0 for AM, 1 for PM
  ind = 0 if AM_PM == "AM" else 1
  dayNum = 0

  add_hours = int(duration.split(":")[0])
  add_minutes = int(duration.split(":")[1])

  new_minutes = start_minutes + add_minutes
  if new_minutes > 60:
    new_minutes -= 60
    add_hours += 1
  
  new_hours = start_hours
  for hour in range(add_hours):
    new_hours += 1
    if new_hours == 12:
      new_hours = 0
      ind = 1 if ind == 0 else 0
      dayNum = dayNum + 1 if ind == 0 else dayNum
  
  if new_hours == 0 : new_hours = 12
    
  AM_PM = "AM" if ind == 0 else "PM"
  new_time = f'{new_hours}:{str(new_minutes).rjust(2, "0")} {AM_PM}'
  
  if day is not None:
    for index in range(len(days)):
      if days[index] == day.lower():
        for i in range(dayNum):
          index += 1
          if index > 6: index = 0          
        break
    
    new_time += f', {days[index].capitalize()}'
  
  additionalString = " (next day)" if dayNum == 1 else f" ({dayNum} days later)" if dayNum > 1 else ""
  new_time += additionalString
  
  return new_time