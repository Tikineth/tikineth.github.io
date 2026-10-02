def calc_average():
    print("Please enter the scores out of 100")
    test = 0
    for i in range(1,6):
        test += int(input(f"Test {i} score: "))
    average = test/5
    print(f"The test score average is: {average}")

def determine_grade(score):
    if (score >= 90):
        return "A"
    elif(score < 90 and score >= 80):
        return "B"
    elif(score < 80 and score >= 70):
        return "C"
    elif(score < 70 and score >= 60):
         return "D"
    elif(score < 60):
         return "F"

calc_average()

for i in range(100, 58, -1):
    print(f"Test score of {i} with a letter grade of {determine_grade(i)}")