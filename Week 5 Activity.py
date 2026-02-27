# 1. Create an empty list
users = []

while True:
    # 2. Display menu
    print("\nUser Management System")
    print("1. Show Users")
    print("2. Add User")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # Show Users
    if choice == "1":
        if len(users) == 0:
            print("No users found.")
        else:
            print("User List:")
            for i in range(len(users)):
                print(f"{i + 1}. {users[i]}")

    # Add User
    elif choice == "2":
        new_user = input("Enter new user name: ")
        users.append(new_user)
        print("User added successfully.")

    # Update User
    elif choice == "3":
        if len(users) == 0:
            print("No users to update.")
        else:
            for i in range(len(users)):
                print(f"{i + 1}. {users[i]}")
            index = int(input("Enter user number to update: ")) - 1

            if 0 <= index < len(users):
                updated_name = input("Enter new name: ")
                users[index] = updated_name
                print("User updated successfully.")
            else:
                print("Invalid user number.")

    # Delete User
    elif choice == "4":
        if len(users) == 0:
            print("No users to delete.")
        else:
            for i in range(len(users)):
                print(f"{i + 1}. {users[i]}")
            index = int(input("Enter user number to delete: ")) - 1

            if 0 <= index < len(users):
                deleted_user = users.pop(index)
                print(f"{deleted_user} deleted successfully.")
            else:
                print("Invalid user number.")

    # Exit
    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")