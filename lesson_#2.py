seconds_per_hours = 60 * 60
seconds_per_day = seconds_per_hours * 24
result = seconds_per_day / seconds_per_hours
result_two = seconds_per_day // seconds_per_hours
print(f'{seconds_per_hours} seconds per hour')
print(f'{seconds_per_day} seconds per day')
print(f'{result} if we divide seconds per day to seconds per hour')
print(f'{result_two} if we integer divide seconds per day to seconds per hour')