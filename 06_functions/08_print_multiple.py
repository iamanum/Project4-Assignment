def repeat_sentence(sentence: str, count: int):
    """Print the sentence the specified number of times."""
    for _ in range(count):
        print(sentence)

def main():
    user_sentence = input("Please enter a sentence: ")
    try:
        repeat_count = int(input("How many times would you like to print the sentence? "))
        repeat_sentence(user_sentence, repeat_count)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
