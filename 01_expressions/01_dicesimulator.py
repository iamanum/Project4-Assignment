# Import the random library to generate random numbers
import random

# Constant for the number of sides on each die
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    # Randomly roll two dice
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    
    # Calculate the total of both dice
    total = die1 + die2
    
    # Print the result of the dice roll
    print(f"Rolled {die1} and {die2}, total: {total}")

def main():
    """
    Main function to simulate rolling dice three times
    """
    print("Rolling the dice three times...")
    
    # Roll the dice three times
    roll_dice()
    roll_dice()
    roll_dice()

# Ensure the main() function is called when the script is executed
if __name__ == '__main__':
    main()
