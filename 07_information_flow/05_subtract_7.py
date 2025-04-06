def adjust_number(num: int) -> int:
    """Function to subtract 7 if the number is greater than 7, else add 5."""
    if num > 7:
        return num - 7
    else:
        return num + 5

def main():
    """Main function to ask user for input and apply the adjustment."""
    number = int(input("Enter a number: "))
    result = adjust_number(number)
    
    if number > 7:
        print(f"After subtracting 7: {result}")
    else:
        print(f"After adding 5: {result}")

if __name__ == "__main__":
    main()
