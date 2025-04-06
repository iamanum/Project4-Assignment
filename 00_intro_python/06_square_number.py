# Prompt the user to enter a number
print_number = 'Type a number to see its square: '

# Get the user's input and convert it to a float to allow decimal numbers
input_number = float(input(print_number))

# Calculate the square of the number and print the result
print(f"""The square of {input_number} is {input_number**2}""")
