def add_time(start_time, duration, day=""):
  #Separation
  start_time_list = start_time.split(":")
  process = start_time_list[1].split()

  #Hour and minutes of the first term
  start_hour_number = int(start_time_list[0])
  start_minute_number = int(process[0])
  is_pm = process[1]
  if "AM" in is_pm and start_hour_number == 12:
    start_hour_number = 0
  if "PM" in is_pm and start_hour_number != 12:
    start_hour_number += 12

  #Hour and minutes of the second term
  duration_list = duration.split(":")
  duration_hour_number = int(duration_list[0])
  duration_minute_number = int(duration_list[1])

  #SUM
  final_hour = start_hour_number + duration_hour_number
  final_minute = start_minute_number + duration_minute_number

  days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

  if final_minute >= 60:
    final_minute -= 60
    final_hour += 1

  print_hour = final_hour%24
  whole_hours = final_hour - print_hour
  divided_days = int(whole_hours/24)
  weeks = int(divided_days/7)
  final_hour = print_hour

  if day.lower() in days:
    day_number = days.index(day.lower())
    final_day_number = (day_number + divided_days) % 7
    day = days[final_day_number]

  if final_hour < 12:
    period = "AM"
  else:
    period = "PM"
    final_hour -= 12

  if final_hour == 0:
    final_hour = 12

  if divided_days > 1:
    if day in days:
      return f"{final_hour}:{final_minute:02d} {period}, {day.capitalize()} ({divided_days} days later)"
    else:
      return f"{final_hour}:{final_minute:02d} {period} ({divided_days} days later)"
  elif divided_days == 1:
    if day in days:
      return f"{final_hour}:{final_minute:02d} {period}, {day.capitalize()} (next day)"
    else:
      return f"{final_hour}:{final_minute:02d} {period} (next day)"
  else:
    if day in days:
      return f"{final_hour}:{final_minute:02d} {period}, {day.capitalize()}"
    else:
      return f"{final_hour}:{final_minute:02d} {period}"
    

#tests
print(add_time('3:00 PM', '3:10'))
# Returns: 6:10 PM
print(add_time('11:30 AM', '2:32', 'Monday'))
# Returns: 2:02 PM, Monday
print(add_time('11:43 AM', '00:20'))
# Returns: 12:03 PM
print(add_time('10:10 PM', '3:30'))
# Returns: 1:40 AM (next day)
print(add_time('11:43 PM', '24:20', 'tueSday'))
# Returns: 12:03 AM, Thursday (2 days later)
print(add_time('6:30 PM', '205:12'))
# Returns: 7:42 AM (9 days later)