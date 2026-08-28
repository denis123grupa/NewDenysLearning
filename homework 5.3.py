


number = int(input("Enter your namber :"))


while number > 9:
    new = 1
    for y in str(number):
        new = new * int(y)

    number = new

print(new)


