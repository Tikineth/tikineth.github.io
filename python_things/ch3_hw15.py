sec = int(input("Please enter a number of seconds: " ))
days = 0
hours = 0
mins = 0
secs = 0

while (sec > 0):
    if (sec >= 86400):
        days = days+1
        sec = sec-86400
    elif (sec >= 3600):
        hours = hours+1
        sec = sec-3600
    elif (sec >= 60):
        mins = mins+1
        sec = sec-60
    elif (sec < 60):
        secs = sec
        sec = 0

print (f"{days} days, {hours} hours, {mins} minutes and {secs} seconds")