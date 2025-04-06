def greet_user(user_name: str):
    """Greets the user with a friendly message."""
    print(f"Welcome, {user_name}! 👋 Hope you’re having a great day!")

def main():
    # Ask for user's name
    user_input = input("What’s your name? ")
    
    # Call the function to greet the user
    greet_user(user_input)

if __name__ == '__main__':
    main()
