import random

print("Welcome to the Dice Rolling Game!")

def roll_a_pair_of_dice():
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)
    return die_1, die_2

# Perform the roll and capture the dice results
first_roll, second_roll = roll_a_pair_of_dice()

# Output the results
print(f"Roll 1: {first_roll}")
print(f"Roll 2: {second_roll}")
print(f"Combined total of the rolls: {first_roll + second_roll}")
