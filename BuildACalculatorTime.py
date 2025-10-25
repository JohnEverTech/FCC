

def add_time(start, duration, day_start=None):
    # Get elements of first parameter
    main_hour, period = start.split()
    start_hour, start_minute = map(int, main_hour.split(':'))
    period = period.upper()
    #print(main_hour,period, start_hour, start_minute)

    # Obtain hour of the second parameter
    hour_duration, minute_duration = map(int,duration.split(':'))

    # Make 24h format
    if period == 'PM' and start_hour != 12:
        start_hour += 12
    if period == 'AM' and start_hour == 12:
        start_hour = 00

    # Convert to all to minutes
    total_minute = start_hour * 60 + start_minute + hour_duration * 60 + minute_duration

    # Make the passed days
    minute_day = 24*60
    days = total_minute // minute_day
    remain_minute = total_minute % minute_day

    # Make the hour operation
    new_hour_24 = remain_minute // 60
    new_minute = remain_minute % 60

    # Convert to 12h format
    if new_hour_24 == 0:
        new_hour = 12
        new_period = 'AM'
    elif new_hour_24 < 12:
        new_hour = new_hour_24
        new_period = 'AM'
    elif new_hour_24 == 12:
        new_hour = 12
        new_period = 'PM'
    else:
        new_hour = new_hour_24 - 12
        new_period = 'PM'

    new_time = f"{new_hour}:{new_minute:02d} {new_period}"

    # Make passed days if thrid parameter is given
    if day_start:
        days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        index = days_of_week.index(day_start.strip().lower())
        new_day = days_of_week[(index + days)%7].capitalize()
        new_time += f", {new_day}"

    if days == 1:
        new_time += " (next day)"
    if days > 1:
        new_time += f" ({days} days later)"

    return new_time

print(add_time('5:30 PM', '40:30'))

