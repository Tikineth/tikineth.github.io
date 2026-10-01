def car_stuff():
    loan_payment = float(input("What is your monthly loan payment?: "))
    insurance = float(input("What is your monthly car insurance premium?: "))
    gas = float(input("What is your monthly gas expense?: "))
    oil= float(input("What is your monthly oil change cost: "))
    tires = float(input("What is your monthly tire cost (try to estimate by averaging years between tire changes): "))
    maintenance= float(input("What is your monthly maintence expense?: "))
    tonthly = loan_payment+insurance+gas+oil+tires+maintenance
    print(f"Your monthly total car expenses are: ${tonthly:.2f}")
    print (f"Your average yearly car expense are: ${tonthly*12:.2f} ")

car_stuff()