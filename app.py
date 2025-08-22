import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)

    print("🎯 Welcome to the Guessing Game!")
    print("I have picked a number between 1 and 100. Can you guess it?")

    while True:
        # Take input from user
        guess = int(input("Enter your guess: "))

        # Compare with generated number
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed the number {number_to_guess} correctly!")
            break

# Run the game
guess_the_number()
