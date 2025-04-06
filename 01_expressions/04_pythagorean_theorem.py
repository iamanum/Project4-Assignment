# Prompt the user to input the two lengths of the right-angle triangle
side_1 = float(input("Enter the first length of the right-angled triangle: "))
side_2 = float(input("Enter the second length of the right-angled triangle: "))

# Function to calculate the third side using Pythagorean theorem
def calculate_hypotenuse(a, b):
    # Calculate the hypotenuse (third side)
    hypotenuse = (a**2 + b**2)**0.5
    return hypotenuse

# Calculate the hypotenuse and display the result
result = calculate_hypotenuse(side_1, side_2)
print(f"The length of the third side (hypotenuse) is: {result}")
