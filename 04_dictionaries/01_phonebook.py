phonebk = {}

while True:
    # Display the options
    print("\nEnter an option:")
    print("1. Add a contact")
    print("2. View phone book")
    print("3. Delete contact")
    print("4. Exit")
    
    # Taking the user input for their choice
    ask = input("Choose an option (1-4): ")

    if ask == '':  # Input validation
        print("Invalid option. Please try again.")
        continue
    elif ask == "1":
        # Add a new contact
        print("\nAdd a contact to the phone book")
        print("="*25)
        name = input("Enter name: ")
        number = input("Enter number: ")

        phonebk[name] = number
        cont = input("Contact added. Do you want to add another contact? (y/n): ")
        if cont.lower() != 'y':
            continue
    elif ask == "2":
        # View all contacts in the phone book
        print("\nPhone book")
        print("="*10)
        if not phonebk:  # Check if the phonebook is empty
            print("The phone book is empty.")
        else:
            n = 1
            for name, number in phonebk.items():
                print(f"{n}. {name} : {number}")
                n += 1
    elif ask == "3":
        # Delete a contact from the phone book
        ask_delete = input("Enter the name of the contact you want to delete: ")

        if ask_delete in phonebk:
            confirm = input(f"Are you sure you want to delete {ask_delete}? (y/n): ")
            if confirm.lower() == 'y':
                del phonebk[ask_delete]
                print(f"{ask_delete} has been deleted successfully.")
            else:
                print(f"{ask_delete} was not deleted.")
        else:
            print("Contact not found.")
    elif ask == "4":
        # Exit the program
        print("Thanks for using the phone book!")
        break
    else:
        print("Invalid option. Please try again.")
