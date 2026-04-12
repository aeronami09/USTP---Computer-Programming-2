balance = 1000  # starting balance

while True:
    print("\n--- Money Withdrawal System ---")
    print("1. Withdraw Money")
    print("2. Check Balance")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        try:
            amount = float(input("Enter amount to withdraw: "))

            if amount > balance:
                print("Error: Insufficient funds.")

                while True:
                    print("\nOptions:")
                    print("1. Try Again")
                    print("2. Check Balance")
                    print("3. Exit")

                    option = input("Choose an option: ")

                    if option == "1":
                        break
                    elif option == "2":
                        print("Current Balance:", balance)
                    elif option == "3":
                        print("Exiting program...")
                        exit()
                    else:
                        print("Invalid option.")
            else:
                balance -= amount
                print("Withdrawal successful!")
                print("Remaining Balance:", balance)

        except ValueError:
            print("Error: Invalid input. Please enter a number.")

    elif choice == "2":
        print("Current Balance:", balance)

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")