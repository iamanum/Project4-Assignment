number = int(input("Enter any number to start doubling: "))

while number < 100:
    doubled_value = number * 2
    print(f"{number} doubled is {doubled_value}\n")
    number = doubled_value

print(f"{number} is greater than or equal to 100, so we stopped here.")
