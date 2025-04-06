# Ask the user to input the length of side 1 of a triangle
ask_length_1 = 'Enter the length of side 1 of a Triangle:'

# Ask the user to input the length of side 2 of a triangle
ask_length_2 = 'Enter the length of side 2 of a Triangle:'

# Ask the user to input the length of side 3 of a triangle
ask_length_3 = 'Enter the length of side 3 of a Triangle:'

# Collect the length of side 1 from the user input and convert it to an integer
answer_length_1 = int(input(ask_length_1))  # Convert the input to an integer

# Collect the length of side 2 from the user input and convert it to an integer
answer_length_2 = int(input(ask_length_2))  # Convert the input to an integer

# Collect the length of side 3 from the user input and convert it to an integer
answer_length_3 = int(input(ask_length_3))  # Convert the input to an integer

# Calculate the perimeter by adding the lengths of all sides
perimeter = answer_length_1 + answer_length_2 + answer_length_3  # Add the lengths of the sides

# Display the result with the calculated perimeter of the triangle
print(f"""Perimeter of triangle with sides {answer_length_1}, {answer_length_2}, and {answer_length_3} is: {perimeter}""")
