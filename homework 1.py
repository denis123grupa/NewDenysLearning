
# number = int(input('Enter your number'))
#
# print(number // 1000)
# print(number // 100 % 10)
# print(number // 10 % 10)
# print(number % 10)



# numbers_1 = int(input("Enter your numbers :"))
#
# thousends = numbers_1 // 1000
# hundreds = numbers_1 // 100 % 10
# tens = numbers_1 // 10 % 10
# once = numbers_1  % 10

# print(f"{thousends}\n{hundreds}\n{tens}\n{once}")


numbers = int(input("Enter your numbers :"))

thousends, left_1 = divmod(numbers, 1000)
hundreds, left_2 = divmod(left_1, 100)
tens, once = divmod( left_2, 10)

print(thousends)
print(hundreds)
print(tens)
print(once)
