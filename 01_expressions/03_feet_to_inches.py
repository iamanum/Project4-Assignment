# Prompt user to input the measurement in feet
measurement_in_feet = float(input("Please enter the measurement in feet: "))

# Conversion function to convert feet to inches
def feet_to_inches_converter(feet_value):
    # Calculate inches by multiplying feet by 12
    return feet_value * 12

# Calculate inches from the input feet and print the result
inches = feet_to_inches_converter(measurement_in_feet)
print(f"The measurement of {measurement_in_feet} feet is equal to {inches} inches.")
