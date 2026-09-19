

def find_unique_value(n):

    for value in n:
        summ_value = n.count(value)
        if summ_value < 2:
         return value

result = find_unique_value([1, 2, 1, 1])

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")