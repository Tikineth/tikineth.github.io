import random

n = "the.txt"
month =["january","febuary","march","april","may","june","july","august","september","october","november","december"]
days = [31,28,31,30,31,30,31,31,30,31,30,31]
av = []

with open(n, "w") as f:
    for i in range(365):
        f.writelines(f"{random.randint(1,91)}\n")

with open(n, "r") as f:
    for i in range(len(month)):
        num = 0
        for j in range(days[i]):
            num += int(f.readline())
        av.append(int(num/days[i]))

for i in range(len(month)):
    print(f"{month[i]} average \"the\"s per day: {av[i]}")
 