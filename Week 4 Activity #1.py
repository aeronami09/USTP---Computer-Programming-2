x = 300

A = float(input("Enter your first number: "))
B = float(input("Enter your second number: "))
C = float(input("Enter your third number: "))

# Store them in a dictionary with labels
numbers = {"A": A, "B": B, "C": C}

# Find the minimum difference from x
min_diff = min(abs(value - x) for value in numbers.values())

# Find all numbers that have that minimum difference
closest_numbers = [label for label, value in numbers.items() if abs(value - x) == min_diff]

# Display the result
if len(closest_numbers) == 3:
    print(f"A is {A}, B is {B}, and C with the value of {C} are all equal in closeness, therefore all numbers are closest to {x}")
elif len(closest_numbers) > 1:
    letters = " and ".join(closest_numbers)
    print(f"Numbers {letters} are equally closest to {x}")
else:
    label = closest_numbers[0]
    value = numbers[label]
    print(f"Letter {label} with the value of {value} is the closest to {x}")