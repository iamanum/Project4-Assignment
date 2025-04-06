def count_numbers():
    # Initialize an empty dictionary to store the count of each number
    number_counts = {}

    # Start a loop to collect numbers from the user
    while True:
        try:
            # Prompt user to input a number
            user_input = input("Enter a number (press Enter to stop): ")

            # If the user presses Enter without input, break the loop
            if user_input == "":
                break
            
            # Convert the input to an integer
            number = int(user_input)
            
            # Check if the number is already in the dictionary, if yes, increment the count
            if number in number_counts:
                number_counts[number] += 1
            else:
                # If the number is not in the dictionary, add it with count 1
                number_counts[number] = 1
        except ValueError:
            # If the input is not a valid number, print an error message and prompt again
            print("Please enter a valid number.")
    
    # Return the dictionary containing the counts of numbers
    return number_counts

def display_counts(number_counts):
    # Print the header for the results
    print("\nNumber counts:")
    # Loop through each number and its count to display
    for number, count in number_counts.items():
        print(f"{number} appears {count} times.")
    
    # Display the full dictionary of counts for debugging or additional info
    print(f"\nAll entered numbers: {number_counts}")

def main():
    # Call count_numbers to get the count of user-entered numbers
    number_counts = count_numbers()
    # Call display_counts to show the results
    display_counts(number_counts)

# Command to run the main function when the script is executed
if __name__ == "__main__":
    main()
