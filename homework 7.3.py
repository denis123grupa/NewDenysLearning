

####### metod 1 #######


def find_unique_value(n):
    from decimal import Decimal

    n = [value_1 for value_1 in n if isinstance(value_1, (int, float, Decimal))]

    for value_2 in n:
        summ_value = n.count(value_2)
        if summ_value == 1:
         return value_2

result = find_unique_value([1, 2, 1, 1, "Hello", [1, 2, 3]])

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")


####### metod 2 #######

#
# def find_unique_value(n):
#
#     for value in n:
#         summ_value = n.count(value)
#         if summ_value == 1:
#          return value
#
# result = find_unique_value([1, 2, 1, 1])
#
# assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
# assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
# assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
# print("ОК")