slice_start = []
slice_duration = []

def add_time(start, duration):
    for element in start:
        slice_start.append(element)
    # take the start hour
    hour_start = int(''.join(slice_start[:-6:]))
    print(hour_start)
    # take and formating two digits for start minutes
    minute_start = (''.join(slice_start[-5:-3]))
    print('{:02d}'.format(int(minute_start)))
    # take the AM or PM data    
    midday = ''.join(slice_start[-2::])
    print (midday)

    for element in duration:
        slice_duration.append(element)
    # take the hour duration to add
    hour_duration =int(''.join(slice_duration[:-3:]))
    print (hour_duration)
    # take the minutes to add and give two digits format
    minute_duration = ''.join(slice_duration[-2::])
    print('{:02d}'.format(int(minute_duration)))
    
    # making the adding time to minutes
    minute_to_add_hour = 0
    new_minute = int(minute_start) + int(minute_duration)
    if new_minute == 60:
        new_minute = '{:02d}'.format(0)
        minute_to_add_hour += 1
    elif new_minute > 60:
        minute_to_add_hour = new_minute//60
        new_minute = '{:02d}'.format(new_minute%60)

    print(minute_to_add_hour)
    print(new_minute)

    #making the adding time to hours
    sub_hour_to_add = int(hour_duration) + minute_to_add_hour
    new_hour = int(hour_start) + sub_hour_to_add
    print(sub_hour_to_add)
    print(new_hour)

    # format the hour presentation
    if new_hour % 12 == 0:
        new_hour = 12
    elif new_hour > 12:
        new_hour = new_hour % 12

    print(new_hour)

    # Make the AM/PM variation
    if midday == 'AM':
        if (sub_hour_to_add // 12) % 2 == 0:
            midday = midday
        else:
            midday = 'PM'
        print(midday)

    if midday == 'PM':
        if (sub_hour_to_add // 12) % 2 == 0:
            midday = midday
        else:
            midday = 'AM'
        print(midday)
    
    
    # making days that have passed
    count = 0
    hour_to_add_day = sub_hour_to_add
    while hour_start + hour_to_add_day > 24:
        count += 1
        hour_to_add_day = hour_to_add_day - 24
    print(f'han pasado {count} dias')
    
    # return and formating output
    new_time = f'{new_hour}:{new_minute} {midday}'
    print(new_time)
    
    return new_time

add_time('3:30 PM', '11:00')