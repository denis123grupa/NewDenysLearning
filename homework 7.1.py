

def add_one(some_list):
    new = ""
    for some in some_list:
        new += str(some)
    some_string = str(int(new) + 1)
    new_some_list = [int(y) for y in some_string]

    return new_some_list

result = add_one([1, 2, 3, 4, 5])

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")


##### metod 2 ######
#
# def add_one(some_list):
#
#     new_list = [str(number) for number in some_list]
#     new_string = str(int("".join(new_list)) + 1)
#     result = [int(x) for x in new_string]
#
#     return  result
# #
# print(add_one([1, 2, 3, 4]))
# #
#
# assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
# assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
# assert add_one([0]) == [1], 'Test3'
# assert add_one([9]) == [1, 0], 'Test4'
# print("ОК")