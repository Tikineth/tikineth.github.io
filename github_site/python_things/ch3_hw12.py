purchases = int(input("How many packages have you brought?: "))

if (purchases < 10):
    print("You don't get a discount")
    discount = 1
elif (purchases >= 10 and purchases < 20):
    print("You get a discount of 10%")
    discount = 0.9
elif (purchases >= 20 and purchases < 50):
    print("You get a discount of 20%")
    discount = 0.8
elif (purchases >= 50 and purchases < 100):
    print("You get a discount of 30%")
    discount = 0.7
elif (purchases >= 100):
    print("You reached the maximum discount of 40%")
    discount = 0.6

print(f"The total amount of your purchase is ${purchases*99*discount}")