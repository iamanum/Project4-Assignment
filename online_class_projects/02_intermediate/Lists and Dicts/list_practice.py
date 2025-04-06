print("List Practice")
print("="*15)

# Initial list of fruits
fruits_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

# Print the length of the list
print("Length of the list: ", len(fruits_list))

# Add 'mango' at the end of the list
fruits_list.append("mango")
print("Updated List: ", fruits_list)

print("\n")

# Index game for animals list
print("Index Game")
print("="*15)
print("\n")

animals_list = ['cat', 'dog', 'elephant', 'tiger', 'lion']

# Function to access an index
def access_index(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "No such index exists."

# Function to modify an element at a specific index
def modify_lst(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."

# Function to slice the list between start and end index
def slice_list(lst, start_index, end_index):
    try:
        return lst[start_index:end_index]
    except IndexError:
        return "Index out of range."

# Menu for user interaction
def list_game():
    print("Choose an operation to perform on the list:")
    print("1. Access an element at a specific index")
    print("2. Modify an element at a specific index")
    print("3. Slice the list between indices")
    
    try:
        choice = int(input("Enter the number corresponding to your choice (1/2/3): "))
        if choice == 1:
            index = int(input("Enter index to access: "))
            print("Element at index:", access_index(animals_list, index))
        elif choice == 2:
            index = int(input("Enter index to modify: "))
            new_value = input("Enter the new value: ")
            print("Updated list:", modify_lst(animals_list, index, new_value))
        elif choice == 3:
            start_index = int(input("Enter start index: "))
            end_index = int(input("Enter end index: "))
            print("Sliced list:", slice_list(animals_list, start_index, end_index))
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Call the list game function
list_game()
