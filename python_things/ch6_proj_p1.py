print("Welcome to the Robo Olympics Club!")
n = int(input("How many teams are there?: "))
rob = "robo.txt"

with open(rob,"w") as f:
    for i in range(n):
        teamn = input("What is the team name?: ")
        rrs = int(input("What is their Robo Rank Score?: "))
        f.writelines(f"Team: {teamn} \n RRS: {rrs} \n")

with open(rob,"r") as f:
    print(f.read())