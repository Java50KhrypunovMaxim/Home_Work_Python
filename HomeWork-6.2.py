user_input = int(input("Enter the number of seconds from 0 to 8640000: "))
hour_in_days = 24
minute_in_hours = 60
seconds_in_minute = 60
seconds_in_hours = minute_in_hours * seconds_in_minute
seconds_in_one_day = hour_in_days * seconds_in_hours

day_counter = user_input // seconds_in_one_day

hour_counter = user_input % seconds_in_one_day // seconds_in_hours

minute_counter = user_input % seconds_in_one_day % seconds_in_hours//seconds_in_minute

second_counter = user_input % seconds_in_one_day % minute_in_hours % seconds_in_minute

print(f"{day_counter}:days  {str(hour_counter).zfill(2)}:{str(minute_counter).zfill(2)}:{str(second_counter).zfill(2)}")