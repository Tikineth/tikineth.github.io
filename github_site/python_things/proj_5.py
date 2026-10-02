import random

def math_equations():
    the_math = random.randint(1,4)
    the_number1 = random.randint(1,100000)
    the_number2 = random.randint(1,100000)
    if (the_math == 1):
        an = the_number2+the_number1
        print(f"      {the_number1}")
        print(f"  +   {the_number2}")
        print(f"--------------")
        answer = int(input("What's the answer?: "))
        if (answer == an):
            print("Congrats you did it!")
        else:
            print("Incorrect. Are you dumber than a 10 year old?")
    elif (the_math == 2):
            an = the_number1-the_number2
            print(f"      {the_number1}")
            print(f"  -   {the_number2}")
            print(f"--------------")
            answer = int(input("What's the answer?: "))
            if (answer == an):
                print("Congrats you did it!")
            else:
                print("Incorrect. Are you dumber than a 10 year old?")
    elif (the_math == 3):
            an = the_number1/the_number2
            print(f"{the_number1} / {the_number2}")
            answer = int(input("What's the answer?: "))
            if (answer == an):
                print("Congrats you did it!")
            else:
                print("Incorrect. Are you dumber than a 10 year old?") 
    elif (the_math == 4):
            an = the_number1*the_number2
            print(f"{the_number1} * {the_number2}")
            answer = int(input("What's the answer?: "))
            if (answer == an):
                print("Congrats you did it!")
            else:
                print("Incorrect. Are you dumber than a 10 year old?")

math_equations()