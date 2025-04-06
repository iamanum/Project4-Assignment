import random

N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

def main():
    # Create a list of 10 random numbers
    random_numbers = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]
    
    # Print each number in the list
    for num in random_numbers:
        print(num)

if __name__ == '__main__':
    main()
