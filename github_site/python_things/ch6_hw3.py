file1 = "bob"

with open(file1, "w") as file:
    for i in range(13):
	    file.writelines(f"wnperfuhwr{i}\n")

with open(file1,"r") as file:
    for pos, line in enumerate(file): 
        print(pos+1, line)