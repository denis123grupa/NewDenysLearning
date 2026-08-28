

number = input("Enter your namber :")
new = 1



for x in number:
    new = new * int(x)

while new > 9:
    new_list = 1

    for y in str(new):
        new_list = new_list * int(y)

    new = new_list
print(new)

