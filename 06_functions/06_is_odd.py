def check_parity(numbers_list):
    """Check if numbers are even or odd and print the result."""
    for number in numbers_list:
        if number % 2 == 0:
            print(f"{number} is even.", end=" ")
        else:
            print(f"{number} is odd.", end=" ")

def main():
    numbers = []
    while True:
        user_input = input("Enter a number (or press Enter to stop): ")
        if user_input == "":
            break
        else:
            try:
                num = int(user_input)
                numbers.append(num)
            except ValueError:
                print("Please enter a valid number.")
                
    check_parity(numbers)

if __name__ == "__main__":
    main()
