while True:
    try:
        # Prompt the user for height input
        height = input("How tall are you? (Leave blank to stop) ")

        # If the user leaves the input blank, break the loop and stop
        if height == "":
            print("Exiting the program. Have a great day!")
            break
        
        # Convert the height to an integer
        height = int(height)

        # Check if the user is tall enough to ride
        if height >= 50:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

    except ValueError:
        # Handle the case where input is not a valid number
        print("\nYou haven't entered a valid height.")
        break  # Stop the loop if the input is invalid
