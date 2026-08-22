value = int(input("Enter your number  :"))

days = 0
one_day = 24 * 60 * 60
one_hour = 60 * 60
one_minute = 60
seconds = 0



if value >= 0 and value < 8640000:

    days, hours = divmod(value, one_day)
    hours, minutes = divmod(hours, one_hour)
    minutes, seconds = divmod(minutes, one_minute)

    full_hours = (str(hours)).zfill(2)
    full_minutes = (str(minutes)).zfill(2)
    full_seconds = (str(seconds)).zfill(2)

    if days < 10:
        result = f"{days} day, {full_hours}:{full_minutes}:{full_seconds}"
    else:
        result = f"{days} days, {full_hours}:{full_minutes}:{full_seconds}"
    print(result)



else:
    print("Your number does not meet the condition")