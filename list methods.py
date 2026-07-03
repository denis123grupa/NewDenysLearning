
# append добовляет в конце значение
number = [1, 2, 3]
number.append(4)
print(number)

# remove удаляет по значению
number_1 = [1, 2, 3, 4]
number_1.remove(3)
print(number_1)

# pop удаляет последний элемент

number_2 = [1, "apple", 2.3]
number_2.pop()
print(number_2)

# insert вставляет элемент в нужное место

number_3 = ["apple1", 3, True]
number_3.insert(1, "orange")
print(number_3)

# clear удоляет все
number_4 = [1, "apple", None]
number_4.clear()
print(number_4)

# index находит индекс элемента
number_5 = [1, "orange", 2.5]
print(number_5.index("orange"))

# count считает колличество одинаковых элементов
number_6 = [1, 2, 1, 3, 1]
print(number_6.count(1))

# sort сортирует список
number_7 = [1, 4, 6, 3, 8]
number_7.sort()
print(number_7)

# revers розварачивает список
number_8 = [1, 2, 3, 4]
number_8.reverse()
print(number_8)