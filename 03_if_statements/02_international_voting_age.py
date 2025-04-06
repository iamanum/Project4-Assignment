# Ask the user to input their age
age = int(input("Please enter your age: "))

# Check the age and print corresponding message based on voting eligibility
if 16 <= age <= 25:
    print("You are eligible to vote in Peturksbouipo, but not in Stanlu and Mayengu.")
elif 26 <= age <= 48:
    print("You can vote in both Peturksbouipo and Stanlu, but not in Mayengu.")
elif age > 48:
    print("You are eligible to vote in all three countries.")
else:
    print("You cannot vote in any of the three countries yet.")
