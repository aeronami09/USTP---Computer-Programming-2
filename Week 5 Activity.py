users = []

while True:
    print("\nUser Management System")
    print("1. Show Users")
    print("2. Add User")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    # For Show Users
    if choice == "1":
        if len(users) == 0:
            print("No users found.")
        else:
            print("\nUser List:")
            for i in range(len(users)):
                print(f"{i + 1}. {users[i]}")

    # For Add User
    elif choice == "2":
        new_user = input("\nEnter new user name: ")
        users.append(new_user)
        print("User added successfully.")

    # For Update User
    elif choice == "3":
        if len(users) == 0:
            print("No users to update.")
        else:
            for i in range(len(users)):
                print(f"{i + 1}. {users[i]}")
            index = int(input("\nEnter user number to update: ")) - 1
    
    # Mag check if ang calculated index is within the range sa atong list
            if 0 <= index < len(users):
                updated_name = input("\nEnter new name: ")
                users[index] = updated_name
                print("User updated successfully.")
            else:
                print("Invalid user number.")

    # For Delete User
    elif choice == "4":
        if len(users) == 0:
            print("No users to delete.")
        else:
            for i in range(len(users)):
                print(f"{i + 1}. {users[i]}")
            index = int(input("\nEnter user number to delete: ")) - 1

    # If atong inputted number is naay value, iya to i delete
            if 0 <= index < len(users):
                deleted_user = users.pop(index)
                print(f"\n{deleted_user} deleted successfully.") 
            else:
                print("Invalid user number.")

    # Exit
    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
