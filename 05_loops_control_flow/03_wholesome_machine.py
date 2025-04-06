sentence: str = "I am capable of achieving anything I set my mind to."

def main():
    print("Please type the following affirmation: " + sentence)

    user_input = input()  
    while user_input != sentence:  
        print("Oops, that's not quite it. Try again!")

        print("Please type the following affirmation: " + sentence)
        user_input = input()

    print("Great job! You've got it! :)")

if __name__ == '__main__':
    main()
