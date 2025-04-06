def get_user_data():
    """Function to prompt the user for their first name, last name, and email."""
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email_address = input("Enter your email address: ")
    return first_name, last_name, email_address

def main():
    """Main function to handle user input and display the received data."""
    user_info = get_user_data()
    print("\nReceived data from user:")
    print(f"First Name: {user_info[0]}")
    print(f"Last Name: {user_info[1]}")
    print(f"Email Address: {user_info[2]}")

if __name__ == "__main__":
    main()
