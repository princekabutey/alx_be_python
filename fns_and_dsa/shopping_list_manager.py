#Initialize an empty shopping list
shopping_list = []

def display_menu():
    """Display the shopping list menu"""
    print(f"Shopping List Manager")
    print(f"---------------------")
    print(f"1. Add Item")
    print(f"2. Remove Item")
    print(f"3. View List")
    print(f"4. Exit")

def add_item():
    """Add an item to the shopping list"""
    item = input("Enter item name: ")
    shopping_list.append(item)
    print(f"Added '{item}' to the list.")

def remove_item():
    """Remove an item from the shopping list"""
    item = input("Enter item name to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"Removed '{item}' from the list.")
    else:
        print(f"'{item}' not found in the list.")

def view_list():
    """Display the current shopping list"""
    if shopping_list:
        print(f"\nCurrent Shopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
    else:
        print("Your shopping list is empty.")

def main():
    shopping_list = []
    """Main function to manage the shopping list"""
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            #prompt for and add an item pass
            add_item()
        elif choice == "2":
            # prompt for and remove an item pass
            remove_item()
        elif choice == "3":
            # Display the shopping list pass
            view_list()
        elif choice == "4":
            print("Goodbye!.")
            break
        else:
            print("Invalid choice. please try again.")

if __name__ == "__main__":
    main()
