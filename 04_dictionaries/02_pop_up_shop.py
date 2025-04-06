fruit_list = {
    'mango': 200,
    'banana': 150,
    'jackfruit': 200,
    'pear': 100,
    'grapes': 200
}

total_cost = 0

# Display the available fruits and their prices
print("Available fruits and their prices (per item):")
for fruit, price in fruit_list.items():
    print(f"{fruit.capitalize()}: {price} per unit")

# Asking the user to choose fruits and calculate the total cost
for fruit, price in fruit_list.items():
    while True:
        try:
            amount = int(input(f"\nHow many {fruit}s would you like to buy? "))
            if amount < 0:
                print("Please enter a valid number of fruits (cannot be negative).")
                continue
            total_cost += amount * price
            break  # Exit the loop once a valid input is received
        except ValueError:
            print("Invalid input. Please enter a number.")

# Display the total cost
print(f"\nTotal cost: {total_cost}")
