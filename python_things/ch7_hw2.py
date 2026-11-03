nummies = []

for i in range(1,21):
    nummers = int(input(f"Enter number {i}: "))
    nummies.append(nummers)

print(max(nummies))
print(min(nummies))
print(sum(nummies))
print(sum(nummies)/20)
