def add_time(start, duration, day=''):
    days_of_the_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    
    start_time, period = start.split()
    split_time = start_time.split(':')
    start_hour = int(split_time[0])
    start_minute = int(split_time[1])
    
    if period == 'PM' and start_hour != 12:
        start_hour += 12
    elif period == 'AM' and start_hour == 12:
        start_hour = 0
    
    start_minutes = start_hour * 60 + start_minute  
    split_duration = duration.split(':')
    duration_hours = int(split_duration[0])
    duration_minutes = int(split_duration[1])
    duration_minutes_total = duration_hours * 60 + duration_minutes  
    
    total_minutes = start_minutes + duration_minutes_total
    new_minutes = total_minutes % 60
    new_hours = int((total_minutes / 60) % 24)
    days_later = int(total_minutes / (60 * 24))
    new_day = ""
    
    if day:
        day_index = 0
        for i in range(len(days_of_the_week)):
            if days_of_the_week[i].lower() == day.lower():
                day_index = i
                break
        new_day = days_of_the_week[(day_index + days_later) % 7]
    
    if new_hours == 0:
        new_period = 'AM'
        new_hour = 12
    elif new_hours == 12:
        new_period = 'PM'
        new_hour = 12
    elif new_hours > 12:
        new_period = 'PM'
        new_hour = new_hours - 12
    else:
        new_period = 'AM'
        new_hour = new_hours

    if new_minutes < 10:
        new_minutes = "0" + str(new_minutes)
    else:
        new_minutes = str(new_minutes)
    
    formatted_time = str(new_hour) + ":" + new_minutes + " " + new_period
    
    if new_day:
        formatted_time += ", " + new_day
    
    if days_later == 1:
        formatted_time += " (next day)"
    elif days_later > 1:
        formatted_time += " (" + str(days_later) + " days later)"
    
    return formatted_time