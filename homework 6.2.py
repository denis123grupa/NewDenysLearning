

def second_index(text, some_str):
    first_index = text.find(some_str)
    target_index = text.find(some_str, first_index + 1)
    if target_index == -1:
        return  None
    else:
        return  (target_index)


(second_index("Hello, hello", "lo"))


assert second_index("sims", "s") == 3, 'Test1'

assert second_index("find the river", "e") == 12, 'Test2'

assert second_index("hi", "h") is None, 'Test3'

assert second_index("Hello, hello", "lo") == 10, 'Test4'

print('ОК')