numbers_1 = int(input("Enter the first number: "))
numebrs_2 = input("Enter the operation:")
numebrs_3 = int(input("Enter the second number:"))

match numebrs_2:
    case "+":
        print(int(numbers_1 + numebrs_3))
    case "-":
         print(int(numbers_1 - numebrs_3))
    case "*":
         print(int(numbers_1 * numebrs_3))
    case "/":
         if numebrs_3 != 0: print(int(numbers_1 / numebrs_3))
         elif numebrs_3 == 0: print("Cannot divide by zero")
