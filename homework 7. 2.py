import string

def is_palindrome(string_1):
    new_string = ""


    for x in string_1:
        if x.isalpha() or x.isdigit():
            y = x.lower()
            new_string += y


    new_1 = new_string[::-1]

    if new_string == new_1:
        return  True
    else:
        return False

print(is_palindrome("A man, a plan, a canal: Panama"))

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'


print("ОК")