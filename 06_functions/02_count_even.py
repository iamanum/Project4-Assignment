def display_even_numbers(lst):
    print("\nEven numbers in the list:")
    print("=" * 30)

    # Loop through the list and print even numbers
    for num in lst:
        if num % 2 == 0:
            print(num, end=" ")

def main():
    numbers = []
    while True:
        user_input = input("Please enter a number (or press Enter to finish): ")
        if user_input == "":
            break
        # Ensure the input is a valid integer before adding it to the list
        try:
            numbers.append(int(user_input))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    display_even_numbers(numbers)

if __name__ == '__main__':
    main()
