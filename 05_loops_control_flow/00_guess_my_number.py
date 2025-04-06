import random

def guess_num():
    num = int(input("Please specify the maximum number up to which the computer can generate a random number: "))
    computer_guess = random.randint(1, num)

    attempts = 0
    guess = None

    print(f"Let's play! Try to guess the secret number between 1 and {num}. Are you ready?")

    while guess != computer_guess:
        try:
            guess = int(input("Take a shot! What's your guess? "))
            attempts += 1

            if guess > computer_guess:
                print("Hmm, that’s a bit too high. Lower it down a bit!")
            elif guess < computer_guess:
                print("Not quite there yet! Try guessing a higher number.")
        except ValueError:
            print("Oops! That’s not a valid number. Please enter a valid integer.")

    print(f"Congratulations! You’ve cracked it! The number was {computer_guess}, and you guessed it in {attempts} attempts!")

if __name__ == "__main__":
    guess_num()
