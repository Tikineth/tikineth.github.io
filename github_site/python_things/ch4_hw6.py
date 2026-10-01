workhours = int(input("How many days do you plan to work?: "))
money = 0.01
total = 0
for i in range(workhours):
    print(f"Day {i+1}    ${money}")
    total += money
    money *= 2

print(f"Total Pay: ${money}")