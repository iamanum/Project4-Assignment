# Ask the user to input a year
year = int(input("Enter a year: "))

# Explanation of leap year conditions
print(f"""A year is a leap year if:
- It is divisible by 4, and
- If it is divisible by 100, it must also be divisible by 400 to be a leap year.""")

# Displaying the divisibility check results for the user
print(f"\nDivisible by 4: {year % 4 == 0}")
print(f"Divisible by 100: {year % 100 == 0}")
print(f"Divisible by 400: {year % 400 == 0}")

# Checking if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("It's a leap year!")
else:
    print("It's not a leap year.")
