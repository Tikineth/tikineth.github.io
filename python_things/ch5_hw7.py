import random

def quiz():
    num = random.randint(1, 1000)
    num1 = random.randint(1, 1000)
    an = num+num1
    print(f"      {num}")
    print(f"  +   {num1}")
    print(f"--------------")
    answer = int(input("What's the answer?: "))
    if (answer == an):
        print("Congrats you did it!")
    else:
        print("Incorrect. Are you dumber than a 10 year old?")

quiz()