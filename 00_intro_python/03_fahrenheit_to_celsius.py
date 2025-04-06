# Ask the user for the temperature in Fahrenheit
ask_question = "Enter the temperature in Fahrenheit: "

# Capture the user's input and store it in the variable 'fahrenheit'
fahrenheit = input(ask_question)

# Convert the input from string to float for mathematical calculations
fahrenheit = float(fahrenheit)

# Calculate the temperature in Celsius using the formula
celsius = (fahrenheit - 32) * 5/9

# Display the result
print(f"""The temperature in Celsius is: {celsius:.2f}°C""")
