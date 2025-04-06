def shorten(lst):
    print("Original list:", lst)  # Command to show the original list

    try:
        # Pop elements from the list until it's empty
        while len(lst) > 0:
            print(f"Before pop: {lst}")  # Command showing the list before popping
            lst.pop()  # Remove the last element of the list
            print(f"After pop: {lst}")  # Command showing the list after popping
            
        print("All items have been removed from the list.")  # Command when list is empty
    except IndexError:
        print("No items left in the list")  # Error message in case of issues

def main():
    # Initialize the list with some values
    new_lst = [2, 3, 4]
    print("Starting the process of shortening the list.")  # Command indicating process start
    shorten(new_lst)
    print("Process complete.")  # Command indicating process completion

if __name__ == "__main__":
    main()
