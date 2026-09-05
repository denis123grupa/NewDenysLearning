

# my_list = [1, 2, 3, 9, 4, 5, 6, 7, 8]
#
# separater = len(my_list) - len(my_list) // 2
# new_list = [my_list[:separater], my_list[separater:]]
#
# print(new_list)

#
# my_list = [1, 2, 3, 9, 4, 5, 6, 7, 8]
#
# separater = 0
#
# if len(my_list) % 2 == 0:
#     separater = len(my_list) // 2
# else:
#     separater = (len(my_list) // 2) + 1
#
# new_list = [my_list[:separater], my_list[separater:]]
#
# print(new_list)



my_list = [1, 2, 3, 9, 4, 5, 6, 7, 8]

separater = len(my_list) // 2

if len(my_list) % 2 !=0:
    separater += 1

new_list = [my_list[:separater], my_list[separater:]]

print(new_list)
















#
# if len(my_list) // 2 != 0:
#
# new_list = my_list[:seporator]
#
# print(new_list)