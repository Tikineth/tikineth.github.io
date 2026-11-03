correct = ["A", "C", "A", "A", "D", "B", "C", "A", "C", "B", "A", "D", "C", "A", 'D', "C", "B", "B", 'D', "A"]
ans = []

for i in range(20):
    q = input(f"What is your answer to question {i+1}?: ")
    if q == correct[i]:
        ans.append(1)
    else:
        ans.append(0)
print("")
if sum(ans) >= 15:
    print(f"You passed! {sum(ans)} correct answers and {20-sum(ans)} incorrect answers")
else:
    print(f"You failed. {sum(ans)} correct answers and {20-sum(ans)} incorrect answers")

for i in range(20):
    if ans[i] == 0:
        print(f"Incorrect Answer at Q{i+1}")