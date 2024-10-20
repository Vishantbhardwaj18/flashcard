class Flashcard:
    """A class to represent a flashcard."""
    
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


class FlashcardQuiz:
    """A class to represent the flashcard quiz."""

    def __init__(self):
        self.flashcards = []

    def add_flashcard(self, question, answer):
        """Add a flashcard to the quiz."""
        self.flashcards.append(Flashcard(question, answer))

    def start_quiz(self):
        """Start the quiz."""
        score = 0
        print("Welcome to the Flashcard Quiz!")
        print("Type 'exit' to quit at any time.\n")

        for flashcard in self.flashcards:
            user_answer = input(f"Question: {flashcard.question} ")
            
            if user_answer.lower() == 'exit':
                print("Thank you for playing!")
                break
            
            if user_answer.strip().lower() == flashcard.answer.lower():
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {flashcard.answer}\n")

        print(f"Your final score: {score}/{len(self.flashcards)}")


def main():
    """Main function to run the quiz."""
    quiz = FlashcardQuiz()
    
    # Adding some flashcards
    quiz.add_flashcard("What is the capital of France?", "Paris")
    quiz.add_flashcard("What is 2 + 2?", "4")
    quiz.add_flashcard("What is the largest planet in our solar system?", "Jupiter")
    quiz.add_flashcard("What is the chemical symbol for water?", "H2O")
    quiz.add_flashcard("Who wrote 'Romeo and Juliet'?", "Shakespeare")

    # Start the quiz
    quiz.start_quiz()


if __name__ == "__main__":
    main()
