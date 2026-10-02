
# option 1


# def popular_words(my_tekst, my_list):
#     new_list = my_tekst.lower()
#     new_list_1 = new_list.split(" ")
#
#     my_result = {}
#     for x in my_list:
#         result = new_list_1.count(x)
#         my_result.update({x: result})
#     return my_result
#
# print(popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']))
#
# assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
# print('OK')


# option 2

# def popular_words(my_str, my_list):
#     def list_lowercase_only(my_str):
#         new_list_1 = [x for x in my_str.lower().split(" ")]
#         return new_list_1
#
#     new_list_1 = list_lowercase_only(my_str)

#     def count_values_to_dict(new_list_1, my_list):
#         result = {}
#         for x in my_list:
#             summ_count = new_list_1.count(x)
#             result.update({x: summ_count})
#         return result
#
#     return count_values_to_dict(new_list_1, my_list)
#
# print(popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']))
# assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
# print('OK')


# option 3

# def popular_words(my_tekst, my_list):
#     new_list = my_tekst.split(" ")
#     new_list_1 = list(map(lambda x: x.lower(), new_list))

#     my_result = {}
#     for x in my_list:
#         result = new_list_1.count(x)
#         my_result.update({x: result})
#     return my_result

# print(popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']))
#
# assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
# print('OK')
