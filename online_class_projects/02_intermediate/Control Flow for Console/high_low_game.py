import random

total_rounds = 5
your_score = 0
computer_score = 0

# Display intro message
print("Welcome to the High-Low Game!")
print("=" * 30)

for round_num in range(1, total_rounds + 1):
    print(f"Round {round_num}")
    print("-" * 20)
    
    # Computer generates a random number
    computer_number = random.randint(1, 100)
    
    # User gets a random number
    user_number = random.randint(1, 100)
    
    print(f"Your number is: {user_number}")
    
    # User guesses whether their number is higher or lower
    guess = input("Do you think your number is higher or lower than the computer's number? (h/l): ").lower()
    
    # Logic for win or lose based on the user's guess
    if guess == 'h' and user_number > computer_number:
        print(f"You were right! The computer's number was {computer_number}.")
        your_score += 1
    elif guess == 'l' and user_number < computer_number:
        print(f"You were right! The computer's number was {computer_number}.")
        your_score += 1
    else:
        print(f"You were wrong. The computer's number was {computer_number}.")
        computer_score += 1

    print(f"Your score: {your_score}")
    print(f"Computer's score: {computer_score}")
    print("=" * 24)
    print("\n")

# Display final scores after the game ends
print("Game Over!")
print(f"Final Scores - Your score: {your_score} | Computer's score: {computer_score}")
print("=" * 30)

# Evaluate the performance
if your_score == total_rounds:
    print("Wow! You played perfectly!")
elif your_score >= total_rounds / 2:
    print("Good job! You played really well!")
else:
    print("Better luck next time!")

print("Thanks for playing! Goodbye!")
