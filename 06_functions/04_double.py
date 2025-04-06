def multiply_by_two(n):
    """Returns the number multiplied by 2."""
    return n * 2

def main():
    # Ask the user for a number
    number = int(input("Please enter a number: "))
    result = multiply_by_two(number)
    
    # Display the result
    print(f"The number {number} doubled is {result}.")

if __name__ == '__main__':
    main()
