def seat_cost():
    clA = int(input("How many class A seats were sold?: "))
    clAcost = clA*20
    clB =  int(input("How many class B seats were sold?: "))
    clBcost = clB*15
    clC = int(input("How many class C seats were sold?: "))
    clCcost = clC*10

    print(f"The total income is: {clAcost+clBcost+clCcost}")
seat_cost()