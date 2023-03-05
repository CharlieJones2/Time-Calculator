def add_time(start, duration, weekday=None):

    weekday_i = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}
    weekday_a = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    s_tuple = start.partition(':')
    s_hours = int(s_tuple[0])
    s_mins = int(s_tuple[2].partition(' ')[0])
    am_pm = s_tuple[2].partition(' ')[2]

    d_tuple = duration.partition(':')
    d_hours = int(d_tuple[0])
    d_mins = int(d_tuple[2])

    e_mins = s_mins + d_mins
    if e_mins >= 60:
        s_hours += 1
        e_mins = e_mins - 60
    if e_mins <= 9:
        e_mins = str(e_mins)
        e_mins = f'0{e_mins}'
    else:
        e_mins = e_mins
    e_hours = (s_hours + d_hours) % 12

    if e_hours == 0:
        e_hours = 12
    else:
        e_hours = e_hours
    if e_hours > 12:
        e_hours = e_hours - 12
    if e_hours == 12 and am_pm == 'AM':
        am_pm = 'PM'

    day = int((s_hours + d_hours) / 24)
    if d_hours == 24 and d_mins == 0:
        am_pm = am_pm
    elif d_hours == 24 and s_mins + d_mins > 60 and am_pm == 'AM':
        am_pm = 'AM'
        day += 1
    elif d_hours == 24 and s_mins + d_mins > 60 and am_pm == 'PM':
        am_pm = 'AM'
        day += 1
    elif am_pm == 'PM' and (s_hours + d_hours) > 12:
        day += 1
        am_pm = 'AM'
    elif am_pm == 'AM' and (s_hours + d_hours) > 12:
        am_pm = 'PM'

    if weekday:
        weekday = weekday.lower()
        index = int(weekday_i[weekday]) + day
        if 7 <= index < 14:
            index -= 7
        elif 14 <= index < 21:
            index -= 14
        elif 21 <= index <= 28:
            index -= 21

        day_new = weekday_a[index]
        if day == 1 and d_hours == 24:
            new_time = str(f'{e_hours}:{e_mins} {am_pm}, {day_new} (next day)')
            return new_time
        if day == 1:
            new_time = str(f'{e_hours}:{e_mins} {am_pm}, {day_new} (next day)')
            return new_time
        elif day > 1:
            new_time = str(f'{e_hours}:{e_mins} {am_pm}, {day_new} ({day} days later)')
            return new_time
        else:
            new_time = str(f'{e_hours}:{e_mins} {am_pm}, {day_new}')
            return new_time

    else:
        if am_pm == 'AM' and s_hours + d_hours > 12 and weekday is None and day == 1:
            new_time = str(f'{e_hours}:{e_mins} {am_pm} (next day)')
            return new_time
        elif am_pm == 'AM' and s_hours + d_hours > 12 and weekday is None and day > 1:
            new_time = str(f'{e_hours}:{e_mins} {am_pm} ({day} days later)')
            return new_time
        elif d_hours == 24:
            new_time = str(f'{e_hours}:{e_mins} {am_pm} (next day)')
            return new_time
        else:
            new_time = str(f'{e_hours}:{e_mins} {am_pm}')
            return new_time
