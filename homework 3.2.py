

my_list = [0, 1, 12, 1, 1]
new_list = []


for elements in range(0, len(my_list), 2):
    new_list.insert(0, elements)
x = my_list.pop()

result = new_list * x
print(result)