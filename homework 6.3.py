
#### 1 ####

def common_elements(num_1, num_2):
    list_1 = []
    list_2 = []

    for value_1 in range(num_1):
        if value_1 % 3 == 0:
            list_1.append(value_1)
    set_1 = set(list_1)

    for value_2 in range(num_2):
        if value_2 % 5 == 0:
            list_2.append(value_2)
    set_2 = set(list_2)

    result = set_1.intersection(set_2)

    return result

assert common_elements(100, 100) == {0, 75, 45, 15, 90, 60, 30}
print("OK")



####### 2 #######

#
# def common_elements(num_1, num_2):
#     # """This function is nested inside another function."""
#
#     list_1 = []
#     list_2 = []
#
#     for value_1 in range(num_1):
#         if value_1 % 3 == 0:
#             list_1.append(value_1)
#
#     for value_2 in range(num_2):
#         if value_2 % 5 == 0:
#             list_2.append(value_2)
#     def change(n_1, n_2):
#         result_1 = set(n_1)
#         result_2 = set(n_2)
#         result = result_1.intersection(result_2)
#
#         return result
#
#     return change(list_1, list_2)
#
# print(common_elements(100,100))
#
#
# assert common_elements(100, 100) == {0, 75, 45, 15, 90, 60, 30}
# print("OK")