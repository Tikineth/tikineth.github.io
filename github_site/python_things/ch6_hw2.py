file1 = "bob"
file2 = "britney"
file3 = "flip"

file = open(file1,"w")
for i in range(13):
	file.writelines(f"wnperfuhwr{i}\n")
file.close()
file = open(file2,"w")
for i in range(1092):
	file.writelines(f"q'lkwhdqe{i}\n")
file.close()
file = open(file3,"w")
for i in range(3):
	file.writelines(f"jhkfewghq{i}\n")
file.close()

hello = input("What is the name of the file you need?: ")
with open(hello, "r") as file:
	lines = sum(1 for line in file)
if (lines < 5):
	with open(hello, "r") as fp: 
		print(fp.readlines())
else: 
	fp = open(hello, "r")
	for i in range(5):
		print(fp.readline())
	file.close()