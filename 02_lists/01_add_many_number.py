def sum_elements(numbers_list):
    total = 0
    for number in numbers_list:
        total += number
    return total

# Prompt user for input
input_numbers = input("Please enter numbers separated by semicolons: ")

# Convert input string into a list of integers
numbers = [int(num) for num in input_numbers.split(';')]

# Calculate the sum of the numbers and print it
total_sum = sum_elements(numbers)
print(f"Sum of the entered numbers: {total_sum}")
