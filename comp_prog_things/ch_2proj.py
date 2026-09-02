# name = input("Please enter your name: ")
# initial1 = input("Please enter your first initial: ")
# initial2 = input("Please enter your second initial: ")
# num1 = int(input("Please enter a number: "))
# num2 = int(input("Please enter another number: "))

# print(name + "              " + initial1 + initial2)
# print(str(num1) + " + " + str(num2) + " = " + str(num1 + num2))
# print(str(num1) + " - " + str(num2) + " = " + str(num1 - num2))
# print(str(num1) + " * " + str(num2) + " = " + str(num1 * num2))
# print(f"{num1} / {num2} = {num1 / num2:.2f}")

# for i in range(1, 11):
#     print(f"{num1} * {i} = {num1 * i}") 

# total = 0
# for i in range(1,6):
#     item = int(input("What is the cost of item " +str(i) + "?: "))
#     total = item+total
# print(f"The total cost of the items is: {total}")
# print(f"The sales tax of these items are: {total*.07}")
# print(f"The total of your order is: {total+total*.07}")

# purchase = int(input("what is the cost of the purchase?: "))
# print("Initial Purchase = " + str(purchase))
# print(f"State Sales Tax: {purchase*.05}")
# print(f"County Sales Tax: {purchase*.025}")
# print(f"Total Value: {purchase+purchase*.05+purchase*.025}")

# purchase = int(input("What was the total charge of your meal today?: "))
# tip = purchase*.18
# stax = float(f"{purchase*.07:.2f}")
# print("Your meal was $" + str(purchase))
# print("Your tip percent was 18% and the tip amount is $" + str(tip))
# print("The sales tax was 7% and the tax amount is $" + str(stax))
# print(f"Total cost of the meal after tips and tax is: {stax+tip+purchase}")

day = int(input("Hello, user! Please enter a number 1-7!: "))

if (day < 1 or day > 7):
    print("That isn't a valid number. Choose a number that is one through seven.")

elif(day == 1):
    print("Monday")
elif(day == 2):
    print("Tuesday")
elif(day == 3):

    print("Wednesday")
elif(day == 4):
    print("Thursday")
elif(day == 5):
    print("Friday")
elif(day == 6):

    print("Saturday")
elif(day == 7):

    print("Sunday")