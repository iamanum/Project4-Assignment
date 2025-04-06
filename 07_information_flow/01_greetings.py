def greetings(name: str) -> str:
    """Return a friendly greeting message with a heart emoji for the given name."""
    return f"Greetings with ❤, {name}! Have a wonderful day ahead."

def main():
    while True:
        name = input("Enter your name (or type 'exit' to quit): ")
        
        if name.lower() == 'exit':
            print("Goodbye! Take care! 👋")
            break
        
        print(greetings(name))
        continue

if __name__ == "__main__":
    main()
