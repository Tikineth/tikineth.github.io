print("Welcome to our Weight Loss \'Program\'! Please enter your weight and we can calculate your possible weight loss if you stay on our program. This program follows the average active person and also doesn't account for any conditions or genetic disorders.")
weight = int(input("Please enter your weight: "))

for i in range(6):
    weight -= 4
    print(f"Weight Loss at end of month {i+1}: {weight}")