try:
    file = open("message.txt", "x")
    print("Successfully Created")
    file.close()

except FileExistsError:
    print("File already exist")
    
while True:
    print("---Welcome to Messaging App---")
    print("1. Send Message")
    print("2. View Message")
    print("3. Exit")
    
    choice = input("\nEnter Choice: ")
    
    if choice == "1":
        message = input("Enter your message: ")
        with open("message.txt", "a") as file:
            file.write(message + "\n")
            file.close()
            
            print("Message sent!\n")
            continue
            
    elif choice == "2":
        print("\n---Messages---")
        file = open("message.txt", "r")
        print(file.read())
        file.close()
    
    elif choice == "3":
        print("\nExiting program...")
        break
    
    else:
        print("\nInvalid Choice. Try Again.")
