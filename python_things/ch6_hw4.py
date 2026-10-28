import random
len = int(input("How long should this file be?: "))
thing = "friend"

file = open(thing,"w")
for i in range(len):
	file.writelines(f"{random.randint(1,501)}\n")
file.close()

total=0
try:
	file = open(thing, "r")
	for line in file:
		print(f"{line}")
		total += int(line)
	file.close()
	print(f"\nThere are {len} numbers with a total of {total} points. ")
except IOError:
  print("Where did you put the file?")
except ValueError:
	print("Ay this ain't the right value.")
