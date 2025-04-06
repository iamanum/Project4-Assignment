def in_range(num, low, high):
    """Check if a number is in the specified range (exclusive)."""
    if low < num < high:
        print(f"Yes! {num} is within the range of {low} and {high}.")
    else:
        print(f"Oops! {num} is NOT within the range of {low} and {high}.")

def get_valid_input(prompt):
    """Function to get valid integer input from the user."""
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Please enter a valid integer.")

def main():
    print("Welcome to the Range Checker!")
    
    # Get valid inputs for the number and the range
    number = get_valid_input("Enter the number to check: ")
    low_range = get_valid_input("Enter the lower bound of the range: ")
    high_range = get_valid_input("Enter the upper bound of the range: ")
    
    # Check if the number is within the range and display the result
    in_range(number, low_range, high_range)

if __name__ == "__main__":
    main()
