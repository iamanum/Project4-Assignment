import random

# Take input for the upper limit
num = int(input("Till what number do you want the computer to generate a number? "))

def guess_num(x):
    # Generate a random number between 1 and num
    computer_guess = random.randint(1, x)
    
    guess = None

    # Loop until the user guesses the correct number
    while guess != computer_guess:
        guess = int(input("Guess any number: "))
        
        if guess > computer_guess:
            print("Oops! Too high, guess again.")
        elif guess < computer_guess:
            print("Oops! Too low, guess again.")
    
    print(f"Wow! You guessed it perfectly, and the number was {computer_guess}.")

# Call the function with the user's input
guess_num(num)
