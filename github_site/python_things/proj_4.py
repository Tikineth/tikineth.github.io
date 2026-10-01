import random

print("Welcome to your personal computer assistant. =)")

while(True):
    print("[1] Enter 1 to Generate a Design.")
    print("[2] Enter 2 to Activate Budget Mode.")
    print("[3] Enter 3 to Project Future Income.")
    print("[q] Enter q to quit.")
    choice = input("What would you like to do?: ")

    if (choice == "1"):
        for i in range(7):
            for j in range(7-i):
                print("*", end="")
            print(" ")
    elif (choice == "2" ):
        end = 0
        pay = 0
        expense = int(input("How much did you budget for \"this\" month?: "))
        spend=1
        while(True):
            pay = int(input(f"Amount of Expense #{spend}? (Type -1 to quit.): "))
            end = pay
            if (end <0 ):
                break
            expense -= pay
            spend += 1
        if (expense < 0):
            lottery = random.randint(1000000, 9999999)
            print(f"You are ${expense} over your budget, but the good news is, I found these lottery numbers! {lottery}")
        elif(expense > 0):
            print(f"You are ${expense} under your budget. Good Job!")
        else:
            print("You met your budget.")


    elif (choice == "3" ):
        workhours = int(input("How many days do you plan to work?: "))
        money = 0.01
        total = 0
        for i in range(workhours):
            print(f"Day {i+1}    ${money}")
            total += money
            money *= 2
        print(f"You made a total of ${total:.2f}")
    elif (choice == "q" ):
        print("Thanks again, bye now.")
        break