

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