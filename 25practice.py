# CREATE A PROGRAM CAPABLE FOR DISPLAYING QUESTION TO THE USER LIKE KBC. USE 
# LIST OF DATA TYPE TO STORE QS AND RESPECTIVE CORRECT ANS. DISPLAY THE FINAL
# AMOUNT IS TAKING HOME AFTER PLAYING THE GAME.



questions = [
    "What is the capital of France?",
    "Which planet is known as the Red Planet?",
    "Who wrote 'To Kill a Mockingbird'?",
    "What is the chemical symbol for water?",
    "Who painted the Mona Lisa?"
]

answers = [
    "Paris",
    "Mars",
    "Harper Lee",
    "H2O",
    "Leonardo da Vinci"
]
import sys
def kbc():
    total_questions = len(questions)
    total_amount = 0

    for i in range(total_questions):
        print(f"\nQuestion {i+1}: {questions[i]}")
        user_answer = input("Your answer: ").strip()

        # Check if the answer is correct
        if user_answer.lower() == answers[i].lower():
            print("Correct!")
            # Update the amount based on question number
            total_amount += (i + 1) * 10000
        else:
            print("Sorry, that's incorrect!")
            print(f"The correct answer is: {answers[i]}")

    # Display the final amount
    print("\nCongratulations! You've completed the game.")
    print(f"Total amount won: {total_amount}")

if __name__ == "__main__":
    print("Welcome to Kaun Banega Crorepati (KBC)!\n")
    kbc()

