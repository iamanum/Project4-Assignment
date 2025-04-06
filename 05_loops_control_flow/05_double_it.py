def main():
    # Ask the user to input a number
    curr_value = int(input("Enter a number: "))
    
    # Use a while loop to double the number until it reaches 100 or greater
    while curr_value < 100:
        curr_value = curr_value * 2  # Double the number
        print(curr_value, end=" ")  # Print the current value followed by a space

if __name__ == '__main__':
    main()
