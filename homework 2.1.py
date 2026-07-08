numbers_1 = int(input("Enter the first number: "))
numebrs_2 = input("Enter the operation:")
numebrs_3 = int(input("Enter the second number:"))


if numebrs_2 == "+":
    print(int(numbers_1 + numebrs_3))
elif numebrs_2 == "-":
    print(numbers_1 - numebrs_3)
elif numebrs_2 == "*":
    print(numbers_1 * numebrs_3)
elif numebrs_2 == "/" and numebrs_3 != 0:
    print(numbers_1 / numebrs_3)
else:
    print("Cannot divide by zero")


