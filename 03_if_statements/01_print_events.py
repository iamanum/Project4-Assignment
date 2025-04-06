# Loop through numbers 0 to 19 and print each number multiplied by 2
for i in range(20):
    print(f"Even number: {i * 2}", end=" ")
print("\n")  # Print a newline for clarity

# Create a list of even numbers from 0 to 38 using list comprehension
even_numbers = [2 * i for i in range(20)]

# Print the list of even numbers
print(f"List of even numbers: {even_numbers}")
