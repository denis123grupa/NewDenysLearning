
# option 1

def difference(*args):
    if args == ():
        return 0
    min_value = args[0]
    max_value = args[0]
    for x in args:
        if x < min_value:
            min_value = x
        if x > max_value:
            max_value = x
    result = max_value - min_value

    return round(result, 1)


print(difference(14.2, 2, -1))

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')


# option 2

# def difference(*args):
#     if args == ():
#         return 0
#
#     def my_min_value(*args):
#         min_value = args[0]
#         for x in args:
#             if x < min_value:
#                 min_value = x
#         return min_value
#
#     def my_max_value(*args):
#         max_value = args[0]
#         for x in args:
#             if x > max_value:
#                 max_value = x
#         return max_value
#
#     def first_difference_values(max_value, min_value):
#         return max_value - min_value
#
#
#     min_value = my_min_value(*args)
#     max_value = my_max_value(*args)

#     result = first_difference_values(max_value,min_value)

#     return round(result, 1)
#
#
# print(difference(14.2, 2, -1))
#
# assert difference(1, 2, 3) == 2, 'Test1'
# assert difference(5, -5) == 10, 'Test2'
# assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
# assert difference() == 0, 'Test4'
# print('OK')


# option 3
#
# def difference(*args):
#
#
#     if args == ():
#         return 0
#
#     result = (max(args) - min(args))
#     result = round(result, 1)
#     return result
#
#
# difference(14.2, 2, -1)
#
#
# assert difference(1, 2, 3) == 2, 'Test1'
# assert difference(5, -5) == 10, 'Test2'
# assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
# assert difference() == 0, 'Test4'
# print('OK')




