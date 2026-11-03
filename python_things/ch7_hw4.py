num = int(input("Give me a number: "))

for i in range(2, int(num/2)):
    if num%i == 0:
        print("This is a composite number.")
        break

if num == 3 or num == 5:
    print("This is a prime number")
elif i == int(num/2-1):
    print("This is a Prime number")