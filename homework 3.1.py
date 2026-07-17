my_list = [0, 1, 0, 12, 3, 0]
new_list = []


for new in my_list:
   if new == 0:
       continue
   new_list.append(new)
zero = my_list.count(0)
for x in range(zero):
    new_list.append(0)


print(new_list)