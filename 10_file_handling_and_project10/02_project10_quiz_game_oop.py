"""
================================================================================
LECTURE 100: Python Project 10 - Quiz Game Project (OOP Architecture) (#lec96)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
OOP Architecture of Quiz Game:
1. Model-View-Controller (MVC) jaisa separation of concerns:
   - Model (`Question` class): Har question ka text aur answer encapsulate karta hai.
   - Data Source (`question_data`): Raw questions ka collection (Dictionaries).
   - Controller (`QuizBrain` class):
     * Question number track karta hai.
     * Score track karta hai.
     * Dekhta hai kya questions bache hain (`still_has_questions()`).
     * Agla question display karta hai (`next_question()`).
     * User answer validate karta hai (`check_answer()`).
"""

# --- 1. Question Model Class ---
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


# --- 2. QuizBrain Logic Class ---
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self, simulated_answer=None):
        current_question = self.question_list[self.question_number]
        self.question_number += 1

        prompt = f"Q.{self.question_number}: {current_question.text} (True/False): "
        if simulated_answer is not None:
            user_answer = simulated_answer
            print(prompt + user_answer)
        else:
            user_answer = input(prompt)

        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.strip().lower() == correct_answer.strip().lower():
            self.score += 1
            print("You got it right! 🎉")
        else:
            print("That's wrong. ❌")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")


# --- 3. Question Bank Data ---
raw_question_data = [
    {"text": "Python was created by Guido van Rossum.", "answer": "True"},
    {"text": "Python is a statically typed programming language.", "answer": "False"},
    {"text": "In Python, tuples are mutable data structures.", "answer": "False"},
    {"text": "The 'is' operator checks for memory address equality.", "answer": "True"},
    {"text": "Python supports multiple inheritance.", "answer": "True"}
]


# --- 4. Main Game Execution ---
def run_quiz_demo():
    print("==========================================")
    print("      OOP QUIZ GAME - PYTHON 2026         ")
    print("==========================================")

    # Convert raw dictionary data into list of Question Objects
    question_bank = []
    for item in raw_question_data:
        q_obj = Question(item["text"], item["answer"])
        question_bank.append(q_obj)

    # Initialize QuizBrain
    quiz = QuizBrain(question_bank)

    # Simulated answers for automated verification:
    simulated_answers = ["True", "False", "False", "True", "True"]

    while quiz.still_has_questions():
        ans = simulated_answers[quiz.question_number]
        quiz.next_question(simulated_answer=ans)

    print("==========================================")
    print("You've completed the quiz!")
    print(f"Your final score was: {quiz.score}/{len(question_bank)} (100%!) 🏆")
    print("==========================================")

if __name__ == "__main__":
    run_quiz_demo()
