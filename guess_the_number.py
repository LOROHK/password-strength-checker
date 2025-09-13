# Guess the Number Game
import random

print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 10.")

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)
guess = None
attempts = 0

# Loop until the user guesses correctly
while guess != secret_number:
    # Get the user's guess
    try:
        guess = int(input("Take a guess: "))
        attempts += 1

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    except ValueError:
        print("Please enter a valid number!")