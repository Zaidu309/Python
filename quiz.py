import random

quiz={
     "Which planet has the most moons?" : (["A.earth","B.Saturn","C.Venus","D.Mars"] ,"B"),
      "How many bones do we have in an ear?" : (["A.3","B.7","C.2","D.8"],"A"),
      "In what year did World War II end?" : (["A.1946","B.1943","C.1945","D.1939"],"C"),
      "What company was originally called Cadabra?": (["A.Amazon","B.Flipkart","C.Nokia","D.Wipro"],"A"),
      "Which planet is known as the Red Planet?": (["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"], "B")
     }

questions = list(quiz.keys())
random.shuffle(questions)


user_answers = {}

# Start the quiz
print("Welcome to the Quiz!\n")
for idx, question in enumerate(questions, 1):
    print(f"Question {idx}: {question}")
    options, correct_answer = quiz[question]
    for option in options:
        print(option)

    # Get user's answer
    while True:
        user_input = input("Your answer (A/B/C/D): ").strip().upper()
        if user_input in ["A", "B", "C", "D"]:
            break
        print("Invalid input. Please enter A, B, C, or D.")

    user_answers[question] = user_input
    print()

# Display results
print("Quiz Completed! Here are your results:\n")
score = 0
for question in questions:
    options, correct_answer = quiz[question]
    user_answer = user_answers[question]
    print(f"Question: {question}")
    print(f"Your Answer: {user_answer}")
    print(f"Correct Answer: {correct_answer}")
    print("Correct!" if user_answer == correct_answer else "Wrong!", "\n")
    if user_answer == correct_answer:
        score += 1

# Final score
print(f"Your total score is {score}/{len(questions)}")
