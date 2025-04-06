def find_divisors(number: int):
    """Print all divisors of a given number."""
    print(f"Divisors of {number}:")
    print("*" * 15)
    divisors = [i for i in range(1, number + 1) if number % i == 0]
    print(" ".join(map(str, divisors)))

def main():
    try:
        num = int(input("Please enter a number: "))
        find_divisors(num)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
