import json

with open("questions.json", "r") as f:
    questions = json.load(f)

score = 0

for q in questions:
    print("\n", q["question"])
    ans = input("Your answer: ")

    if ans.lower() == q["answer"].lower():
        score += 1
        print("Correct!")
    else:
        print("Wrong!")

print(f"\nFinal Score: {score}/{len(questions)}")