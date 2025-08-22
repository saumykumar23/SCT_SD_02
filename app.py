
import tkinter as tk
import random
from tkinter import messagebox

class GuessTheNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Guess the Number Game")
        self.root.geometry("400x300")
        
        self.number_to_guess = random.randint(1, 100)

        self.label = tk.Label(root, text="I have picked a number (1-100).\nCan you guess it?", 
                              font=("Arial", 12))
        self.label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=10)

        self.button = tk.Button(root, text="Guess", font=("Arial", 12), command=self.check_guess)
        self.button.pack(pady=10)

        self.feedback = tk.Label(root, text="", font=("Arial", 12))
        self.feedback.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a number between 1 and 100!")
            return
        
        if guess < self.number_to_guess:
            self.feedback.config(text="Too Low! Try again ❌", fg="red")
        elif guess > self.number_to_guess:
            self.feedback.config(text="Too High! Try again ❌", fg="red")
        else:
            self.feedback.config(text=f"🎉 Correct! The number was {self.number_to_guess}", fg="green")
            messagebox.showinfo("Congratulations!", "You guessed the number correctly!")
            self.reset_game()

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.entry.delete(0, tk.END)
        self.feedback.config(text="")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessTheNumberGame(root)
    root.mainloop()
