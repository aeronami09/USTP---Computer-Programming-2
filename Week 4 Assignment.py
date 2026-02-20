print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

# Get two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    result = num1 + num2
    symbol = "+"
elif choice == "2":
    result = num1 - num2
    symbol = "-"
elif choice == "3":
    result = num1 * num2
    symbol = "*"
elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        symbol = "/"
    else:
        result = "undefined (cannot divide by zero)"
        symbol = "/"
else:
    result = None
    symbol = ""
    print("Invalid choice.")

# Display the result if valid
if result is not None:
    print(f"{num1} {symbol} {num2} = {result}")