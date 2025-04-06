def create_sentence(word: str, num: int):
    """Generate a sentence based on the word and the given number."""
    if num == 1:
        print(f"Looking out my {word}, the sky is big and groovy!")
    elif num == 2:
        print(f"Looking out my window, the sky is big and {word}!")
    elif num == 3:
        print(f"Looking out my window, the sky is {word} and groovy!")

def main():
    user_word = input("Enter any word: ")
    print(f"The word {user_word} can be a noun, verb, or adjective. Please choose a category.")
    user_choice = int(input("Choose a number: \n1. Noun \n2. Verb \n3. Adjective: "))
    
    if user_choice in [1, 2, 3]:
        create_sentence(user_word, user_choice)
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
