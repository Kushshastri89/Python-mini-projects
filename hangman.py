import tkinter as tk
from tkinter import messagebox
import random

# Question-answer pairs
questions = [
    {"question": "A programming language named after a snake.", "answer": "python"},
    {"question": "Device used to input letters.", "answer": "keyboard"},
    {"question": "The brain of the computer.", "answer": "processor"},
    {"question": "We use this to browse the internet.", "answer": "browser"},
    {"question": "The short term memory of a computer.", "answer": "ram"}
]

class QuizHangman:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Quiz 🧠")
        self.q_and_a = random.choice(questions)
        self.word = self.q_and_a["answer"].lower()
        self.guessed = []
        self.max_attempts = 6
        self.attempts_left = self.max_attempts

        # UI Components
        self.question_label = tk.Label(root, text="❓ " + self.q_and_a["question"], font=("Arial", 14), wraplength=400)
        self.question_label.pack(pady=10)

        self.word_display = tk.Label(root, text="_ " * len(self.word), font=("Courier", 28))
        self.word_display.pack(pady=20)

        self.attempts_label = tk.Label(root, text=f"Attempts left: {self.attempts_left}", font=("Arial", 14))
        self.attempts_label.pack()

        self.guess_entry = tk.Entry(root, font=("Arial", 18), width=4, justify="center")
        self.guess_entry.pack(pady=10)
        self.guess_entry.focus()

        self.guess_button = tk.Button(root, text="Guess", command=self.process_guess, font=("Arial", 14))
        self.guess_button.pack()

        self.guessed_label = tk.Label(root, text="Guessed: ", font=("Arial", 12))
        self.guessed_label.pack(pady=10)

    def process_guess(self):
        letter = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if not letter.isalpha() or len(letter) != 1:
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
            return

        if letter in self.guessed:
            messagebox.showinfo("Already Guessed", "You already guessed that letter.")
            return

        self.guessed.append(letter)

        if letter not in self.word:
            self.attempts_left -= 1

        self.update_display()

        if self.attempts_left == 0:
            messagebox.showinfo("Game Over", f"You lost! The answer was: {self.word}")
            self.root.destroy()

        elif all(char in self.guessed for char in self.word):
            messagebox.showinfo("You Win!", f"Great job! You guessed the word: {self.word}")
            self.root.destroy()

    def update_display(self):
        display = ' '.join([ch if ch in self.guessed else '_' for ch in self.word])
        self.word_display.config(text=display)
        self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")
        self.guessed_label.config(text=f"Guessed: {', '.join(self.guessed)}")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x400")
    app = QuizHangman(root)
    root.mainloop()
