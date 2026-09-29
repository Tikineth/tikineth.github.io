years = int(input("How many years have passed?: "))
months = 0
month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
rain = 0
for i in range(years):
    print(f"Year {i+1}")
    for j in range(12):
        rain += int(input(f"How many inches of rainfall occured in {month[j]}?: "))
    months += 12

print(f"I see. So it's been {months} months with a total of {rain} inches of rainfall and an average amount of {rain/months} inches of rainfall each month. Very interesting.")