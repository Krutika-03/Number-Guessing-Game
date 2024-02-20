import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize the number of attempts
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I've picked a number between 1 and 100. Try to guess it.")
    
    while True:
        guess = input("Enter your guess (or 'q' to quit): ")
        
        # Check if the user wants to quit
        if guess.lower() == 'q':
            print("The secret number was:", secret_number)
            print("Thanks for playing! Goodbye.")
            break
        
        # Check if the input is a valid number
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        # Convert the input to an integer
        guess = int(guess)
        
        # Increment the number of attempts
        attempts += 1
        
        # Check if the guess is correct
        if guess == secret_number:
            print("Congratulations! You've guessed the number in", attempts, "attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

# Call the function to start the game
guess_number()