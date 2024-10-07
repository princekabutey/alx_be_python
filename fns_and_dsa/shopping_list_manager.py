#Initialize an empty shopping list
shopping_list = []

def display_menu():
    """Display the shopping list menu"""
    print("\nShopping List Manager")
    print("---------------------")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

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
        print("\nCurrent Shopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
    else:
        print("Your shopping list is empty.")

def main():
    """Main function to manage the shopping list"""
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            view_list()
        elif choice == "4":
            print("Exiting the shopping list manager.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
