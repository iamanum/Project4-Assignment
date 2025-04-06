# Define the input prompts with special formatting
prompt_1 = "\033[1m\033[3mEnter the first number: \033[0m"
prompt_2 = "\033[1m\033[3mEnter the second number: \033[0m"

# Take input for the two numbers
first_number = int(input(prompt_1))
second_number = int(input(prompt_2))

# Function to calculate quotient and remainder
def calculate_quotient_and_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

# Call the function and store the result
quotient, remainder = calculate_quotient_and_remainder(first_number, second_number)

# Print the result with formatted output
print(f"The quotient of {first_number} divided by {second_number} is: \033[1m\033[3m{quotient}\033[0m, with a remainder of: \033[1m\033[3m{remainder}\033[0m")
