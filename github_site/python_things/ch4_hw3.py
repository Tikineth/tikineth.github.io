speed = int(input("What is the speed of the vehicle in mph?: "))
time_length = int(input("How many hours has it been traveling?: "))

print("Hour   Distance Traveled")
for i in range(time_length):
    print(f"{i+1}      {(i+1)*speed}")