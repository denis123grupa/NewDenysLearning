list_1 = [1, 2, 3, 4, 5, 6, 7]

elements = len(list_1)

if elements <= 0:
    print([])
elif elements % 2 == 0:
    list_2 = list_1[:4]
    list_3 = list_1[4:]
    list_4 = [list_2] + [list_3]

elif elements % 2 != 0:
    list_2 = list_1[:4]
    list_3 = list_1[4:]
    list_4 = [list_2] + [list_3]

list_2 = list_1[:4]
list_3 = list_1[4:]
list_4 = [list_2] + [list_3]
print(list_4)

