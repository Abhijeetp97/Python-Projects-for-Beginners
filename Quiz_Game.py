import json
import random

def load_questions(filename):
    with open(filename, 'r') as file:
        questions = json.load(file)
    return questions

def quiz(questions, category, difficulty):
    score = 0
    selected_questions = [q for q in questions if q['category'] == category and q['difficulty'] == difficulty]
    
    if not selected_questions:
        print(f"No questions available for category '{category}' and difficulty '{difficulty}'.")
        return

    random.shuffle(selected_questions)

    for q in selected_questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        
        while True:
            answer = input("Your answer (A/B/C/D) or 'Q' to quit: ").strip().upper()
            if answer in ['A', 'B', 'C', 'D']:
                if answer == q["answer"]:
                    score += 1
                    print("Correct!")
                else:
                    print(f"Wrong! The correct answer is {q['answer']}.")
                break
            elif answer == 'Q':
                print("Exiting the quiz...")
                print(f"\nYour final score is: {score}/{len(selected_questions)}")
                return
            else:
                print("Invalid input. Please enter A, B, C, D, or Q.")

    print(f"\nYour final score is: {score}/{len(selected_questions)}")
    print("Thank you for playing the quiz!")

def main():
    print("Welcome to the Quiz Game!")
    filename = input("Enter the name of the JSON file with the quiz questions (e.g., 'questions.json'): ").strip()
    questions = load_questions(filename)
    
    categories = set(q['category'] for q in questions)
    print("Available categories:", ", ".join(categories))
    while True:
        category = input("Choose a category: ").strip()
        if category in categories:
            break
        else:
            print("Invalid category. Please choose a valid category.")

    difficulties = set(q['difficulty'] for q in questions)
    print("Available difficulty levels:", ", ".join(difficulties))
    while True:
        difficulty = input("Choose a difficulty level: ").strip()
        if difficulty in difficulties:
            break
        else:
            print("Invalid difficulty level. Please choose a valid difficulty level.")

    quiz(questions, category, difficulty)

if __name__ == "__main__":
    main()