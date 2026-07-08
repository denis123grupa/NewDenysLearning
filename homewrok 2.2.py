your_list = [1, 2, 3]

result = your_list[-1]
your_list.pop()
your_list.insert(0, result)

print(your_list)


# if len(your_list) == [] or len(your_list) == [1]:
# result = your_list.index(3)
#
# your_list.pop()
#
# your_list.insert(0, your_list)
#
# print(your_list)