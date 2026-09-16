mth = int(input("Please enter the month: "))
day = int(input("Please enter a day: "))
year = int(input("Please enter the last digits of a year: "))

if (day*mth == year):
    print("The date is magic!")
else:
    print("The date is not magic.")