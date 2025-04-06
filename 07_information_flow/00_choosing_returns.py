adult_age = 18

def check_age(age: int) -> bool:
    """Check if the given age qualifies as an adult age."""
    if age >= adult_age:
        print("Entered age is an adult age.")
        return True
    else:
        print("Entered age is not an adult age.")
        return False

def main():
    age = int(input("Enter your age: "))
    check_age(age)  # No need to print the return value here, just call the function

if __name__ == "__main__":
    main()
