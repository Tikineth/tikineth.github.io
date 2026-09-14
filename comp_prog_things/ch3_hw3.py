age = int(input("How old are you?: "))

if (age < 1):
    print("You're an infant.")
elif (age < 13 and age > 1):
    print("You're a child. Have fun playing with your toys!")
elif (age < 20 and age > 13):
    print("You're a teenager. Good luck with puberty!")
elif (age >= 20):
    print("You're an adult.")