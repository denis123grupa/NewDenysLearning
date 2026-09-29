

def popular_words(my_tekst, my_list):
    new_list = my_tekst.lower()
    new_list_1 = new_list.split(" ")
    my_result = {}
    for x in my_list:
        result = new_list_1.count(x)
        my_result.update({x: result})
    return (my_result)

print(popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']))

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')