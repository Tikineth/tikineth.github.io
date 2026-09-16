pennies = int(input("Enter an amount of pennies: "))
nickels = int(input("Enter an amount of nickels: "))*5
dimes = int(input("Enter an amount of dimes: "))*10
quarters = int(input("Enter an amount of quarters: "))*25

maybe_dollar = pennies+nickels+dimes+quarters

if (maybe_dollar == 100):
    print("You won the dollar game!")
elif (maybe_dollar > 100):
    print("That's more than a dollar")
elif (maybe_dollar < 100):
    print("That's less than a dollar.")
