numbers_1 = int(input("Enter the first number: "))
action = input("Enter the operation:")
numbers_3 = int(input("Enter the second number:"))

result = numbers_1 + numbers_3 if action == "+" else (numbers_1 - numbers_3 if action == "-" else (numbers_1 * numbers_3 if action == "*" else (numbers_1 / numbers_3 if numbers_3 != 0 else "Cannot divide by zero" )))
print(result)
a