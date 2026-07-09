score = 0

questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": {
            "A": "function",
            "B": "def",
            "C": "define",
            "D": "func"
        },
        "answer": "B"
    },
    {
        "question": "Which data type stores multiple items in order?",
        "options": {
            "A": "Dictionary",
            "B": "List",
            "C": "Set",
            "D": "Boolean"
        },
        "answer": "B"
    },
    {
        "question": "What is the output of print(5 + 3 * 2)?",
        "options": {
            "A": "16",
            "B": "11",
            "C": "13",
            "D": "10"
        },
        "answer": "B"
    },
    {
        "question": "Which keyword creates a loop that repeats while a condition is true?",
        "options": {
            "A": "for",
            "B": "loop",
            "C": "while",
            "D": "repeat"
        },
        "answer": "C"
    },
    {
        "question": "Which function displays output on the screen?",
        "options": {
            "A": "display()",
            "B": "show()",
            "C": "output()",
            "D": "print()"
        },
        "answer": "D"
    }
]

print("=" * 35)
print("        PYTHON QUIZ GAME")
print("=" * 35)
print("There are", len(questions), "questions.")
print("Each correct answer is worth 1 point.")
input("\nPress Enter to start...")

for i, q in enumerate(questions, start=1):

    print(f"\nQuestion {i}")
    print(q["question"])

    for key, value in q["options"].items():
        print(f"{key}. {value}")

    while True:
        user_answer = input("Your answer: ").upper()

        if user_answer in ["A", "B", "C", "D"]:
            break
        else:
            print("Please enter A, B, C, or D.")

    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Incorrect!")
        print(f"The correct answer was {q['answer']}.")

print("\n" + "=" * 35)
print("          QUIZ FINISHED")
print("=" * 35)

print(f"Score: {score}/{len(questions)}")

percentage = (score / len(questions)) * 100
print(f"Percentage: {percentage:.0f}%")

if percentage == 100:
    print("Outstanding! Perfect score!")
elif percentage >= 80:
    print("Great job!")
elif percentage >= 60:
    print("Good work!")
elif percentage >= 40:
    print("Keep practicing!")
else:
    print("Better luck next time!")