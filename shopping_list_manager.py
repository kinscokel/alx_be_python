# shopping_list_manager.py
def shopping_list():
    print("shopping List Manager")
    print("1. add items to list")
    print("2. remove items from list")
    print("3. display the current list")
    print("4. exit")

def main():
    shopping_list = []
    while true:
        dispaly_menu()
        choice = input("Enter your choices:")
        if choice == '1':
            item = input("Enter the item to add:")
            if item:
                shopping_list.append(item)
                print("{item} has been added to your shopping list.")
            else:
                print("item can not be empty.")
        elif choice == '2':
            item = input("Enter the item to be removed:")
            if item in shopping_list:
                shopping_list.remove(item)
                print("{item} has been removed from your shopping list. ")
            else:
                print("item is not in your shopping list.")
        elif choice == '3':
            if shopping_list:
                print("items in your shopping list")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


