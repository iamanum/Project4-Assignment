# Function to display the list of numbers
def display_list(lst):
    print(f"The numbers in your list are: {lst}")

def main():
    num_list = []  # Initialize an empty list to store the numbers

    # Prompt the user to input numbers
    print("Enter numbers to save in the list. Press Enter to stop.")
    
    while True:
        element = input("Enter a number (or press Enter to stop): ")

        # Stop the loop if the user presses enter without input
        if element == "":
            break

        try:
            # Try to convert the input to an integer
            num_list.append(int(element))
        except ValueError:
            print("Invalid input! Please enter a valid number.")  # Handle non-integer inputs

    # Call the function to display the list of numbers
    display_list(num_list)

# Run the program if this script is executed directly
if __name__ == "__main__":
    main()
