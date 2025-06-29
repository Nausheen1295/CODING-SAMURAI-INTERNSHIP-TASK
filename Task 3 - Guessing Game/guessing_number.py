import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("400x400")
        self.master.resizable(False, False)
        self.master.configure(bg="#222222")

        self.secret_number = random.randint(1, 100)
        self.tries = 0
        self.high_score = float('inf')  # Initialize high score to infinity

        self.title_label = tk.Label(master, text="Guess the number (1 - 100)", font=("Arial", 16), bg="#222222", fg="#ffffff")
        self.title_label.pack(pady=10)

        self.entry = tk.Entry(master, font=("Arial", 14), justify='center')
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(master, text="Guess", font=("Arial", 14), command=self.check_guess, bg="#4CAF50", fg="#ffffff", activebackground="#45a049")
        self.guess_button.pack(pady=5)

        self.result_label = tk.Label(master, text="", font=("Arial", 14), bg="#222222", fg="#ffffff")
        self.result_label.pack(pady=10)

        self.reset_button = tk.Button(master, text="Reset Game", font=("Arial", 12), command=self.reset_game, bg="#f44336", fg="#ffffff", activebackground="#e53935")
        self.reset_button.pack(pady=5)

        self.high_score_label = tk.Label(master, text=f"High Score: {self.high_score}", font=("Arial", 14), bg="#222222", fg="#ffffff")
        self.high_score_label.pack(pady=10)

    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit():
            self.result_label.config(text="❌ Please enter a valid number!")
            return

        guess = int(guess)

        # Check if the guess is within the valid range
        if guess < 1 or guess > 100:
            self.result_label.config(text="❗ Please enter a number between 1 and 100!")
            return

        self.tries += 1

        if guess < self.secret_number:
            self.result_label.config(text="🔻 Too low! Try again.")
        elif guess > self.secret_number:
            self.result_label.config(text="🔺 Too high! Try again.")
        else:
            self.result_label.config(text=f"✅ Correct! You guessed it in {self.tries} tries.")
            self.update_high_score()

    def update_high_score(self):
        if self.tries < self.high_score:
            self.high_score = self.tries
            self.high_score_label.config(text=f"High Score: {self.high_score}")

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.tries = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="Game reset. Try again!")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
