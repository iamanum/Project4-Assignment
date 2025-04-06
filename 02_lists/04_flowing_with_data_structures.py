# This function adds 5 copies of the given 'data' to the 'my_list'
def add_five_copies(my_list, data):
    # Loop 5 times to append the data to the list
    for _ in range(5):
        my_list.append(data)  # Append the data to the list

# This is the main function that runs the program
def main():
    # Ask the user to input a message to copy
    message = input("Enter a message to copy: ")
    
    # Create an empty list where the message will be stored
    my_list = []
    
    # Print the list before adding any data (it will be empty at this point)
    print("List before:", my_list)
    
    # Call the function to add 5 copies of the message to the list
    add_five_copies(my_list, message)
    
    # Print the list after adding the 5 copies of the message
    print("List after:", my_list)

main()
