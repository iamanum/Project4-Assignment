prompt = "What would you like to hear? (type 'joke' or anything else)"
joke = "Here’s a joke for you! Sophia is heading out to the grocery store. A programmer tells her: 'Get a liter of milk, and if they have eggs, get 12.' Sophia returns with 13 liters of milk. The programmer asks why, and Sophia replies: 'Because they had eggs.'"
sorry = "Oops! I don't have that for you."

print(prompt)
user_input = input().lower()  # Makes the input case-insensitive

if user_input == "joke":
    print(joke)
else:
    print(sorry)
