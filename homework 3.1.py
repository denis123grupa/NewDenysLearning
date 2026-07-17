#
#
# # Please run the code, and then follow the instructions on line 22
#
#
# my_list = [0, 1, 12, 0, 0 ]
# new_list = []
#
#
# if 0 not in my_list:
#     print("Zero not found")
# else:
#     for new in my_list:
#         if new == 0:
#             continue
#         new_list.append(new)
#     zero = my_list.count(0)
#     for x in range(zero):
#         new_list.append(0)
#
#
# # Please try removing the zeros or replacing them with other numbers in the my_list variable :
#
#
# if new_list == []:
#     print("Sorry Nikolas, I forgot how to print nothing in this case.")
# else:
#     print(new_list)


my_list = [0, 1, 12, 1, 1 ]
new_list = []


if 0 not in my_list:
    print("Zero not found")
else:
    for new in my_list:
        if new == 0:
            continue
        new_list.append(new)
    zero = my_list.count(0)
    for x in range(zero):
        new_list.append(0)
    print(new_list)