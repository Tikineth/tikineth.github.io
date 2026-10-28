filename = input("Create File name: ")
len = int(input("long: "))
file = open(filename,"w")
for i in range(len):
	file.writelines(f"{i}\n")
file.close()

file = open(filename, "r")
for line in file:
	print(f"{line}")
file.close()

