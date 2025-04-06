def print_ones_digit(num: int):
    """Print the ones digit of a given number."""
    ones_digit = num % 10
    print(f"The ones digit of {num} is {ones_digit}")

def main():
    enter_num = int(input("Enter any number: "))
    print_ones_digit(enter_num)

if __name__ == "__main__":
    main()
