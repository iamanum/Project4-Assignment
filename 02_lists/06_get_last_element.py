# Function to display the last element of the list
def show_last_element(lst):
    if lst:  # Check if the list is not empty
        print(f"The last element in your list is: {lst[-1]}")
    else:
        print("The list is empty, no last element to show.")

def main():
    num_list = []  # Initialize an empty list to store the numbers

    # Prompt the user to input numbers, and stop when they press enter without input
    print("Please enter numbers to save in the list. Press Enter without typing anything to stop.")
    while True:
        element = input("Enter a number (or press Enter to stop): ")
        
        # Break the loop if the user presses enter without input
        if element == "":
            break

        try:
            # Attempt to convert the input to an integer and append to the list
            num_list.append(int(element))
        except ValueError:
            print("That's not a valid number! Please try again.")  # Handle invalid inputs

    # Call the function to display the last element
    show_last_element(num_list)

# Start the program when this script is run
if __name__ == "__main__":
    main()
