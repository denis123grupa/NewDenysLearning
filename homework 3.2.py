


my_list = [0, 1, 12, 1, 1, 5]
# my_list = []
new_list = []

if my_list == []:
    print(0)
else:
    for x in range(0, len(my_list), 2):
      new_list.append(my_list[x])

    summa = 0
    for z in range(len(new_list)):
        summa += (new_list[z])
    times = my_list[-1]
    result = summa * times
    print(result)






