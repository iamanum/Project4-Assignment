import random

def generate_random_numbers():
    try:
        for _ in range(10):
            print(random.randint(1, 100), end=" ")
    except Exception as e:
        print("\nError:", e)

def main():
    print("Generating 10 random numbers between 1 and 100:")
    generate_random_numbers()

if __name__ == "__main__":
    main()
