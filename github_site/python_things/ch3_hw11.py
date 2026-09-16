books = int(input("How many books do you checked out each month?: "))

if (books <= 1):
    print("You have been awarded 0 points.")
elif (books >= 2 and books < 4):
    print("You have been awarded 5 points.")
elif (books >= 4 and books < 6):
    print("You have been awarded 15 points.")
elif (books >= 6 and books < 8):
    print("You have been awarded 30 points.")
elif (books >= 8):
    print("You have been awarded 60 points.")