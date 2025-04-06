# A list of available fruits
fruit = ["apple", "banana", "orange", "grape"]

# Dictionary to store fruit stock count
fruit_stock = {
    "apple": 2,
    "banana": 5,
    "orange": 10,
    "grape": 15
}

def in_stock(name: str):
    """Check if the fruit is in stock and return the stock count."""
    # Convert input to lowercase to handle case-insensitive matching
    name = name.lower()
    
    # Check if the fruit exists in stock and return the stock count
    if name in fruit_stock:
        print(f"{name.capitalize()} is in stock!")
        return fruit_stock[name]
    else:
        print(f"{name.capitalize()} is not in stock.")
        return 0

def main():
    """Main function to interact with the user."""
    # Asking for user input
    ask = input("Enter the fruit name: ").strip()

    # Getting the stock count for the entered fruit
    count_stock = in_stock(ask)

    # Displaying the stock count if available, otherwise a message
    if count_stock != 0:
        print(f"Here's how many we have: {count_stock}")
    else:
        print("Sorry! The fruit is not available.")

if __name__ == "__main__":
    main()
