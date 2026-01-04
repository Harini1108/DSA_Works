#Shopping list manager
shopping_list = []

while True:
    action = input("Enter action (add / remove / show / quit): ").lower()

    if action == "add":
        item = input("Enter item name: ")
        shopping_list.append(item)
        print(item, "added")

    elif action == "remove":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "removed")
        else:
            print("Item not found")

    elif action == "show":
        print("Shopping list:", shopping_list)

    elif action == "quit":
        print("Exiting program")
        break

    else:
        print("Invalid action")