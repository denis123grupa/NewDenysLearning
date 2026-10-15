###### option 1 ######

def is_even(value):
    if value % 2 == 0:
        return True
    else:
        return False

print(is_even(4))

assert is_even(2) == True, 'Test1'

assert is_even(5) == False, 'Test2'

assert is_even(0) == True, 'Test3'

print('OK')

### option 2 #####

def is_even(value):

    if not str(value).strip("-").isdigit():
        return "Sorry, the value is not a digit"
    else:
        return True if value % 2 == 0 else False

print(is_even(-4))

assert is_even(2) == True, 'Test1'

assert is_even(5) == False, 'Test2'

assert is_even(0) == True, 'Test3'

print('OK')

###### option 3 ######

def is_even(value):

    def check_at_int():
        if not str(value).strip("-").isdigit():
            return "Sorry, the value is not a digit"
        else:
            return start_is_even()
    def start_is_even():
        return True if int(value) % 2 == 0 else False

    return check_at_int()

print(is_even("4"))

assert is_even(2) == True, 'Test1'

assert is_even(5) == False, 'Test2'

assert is_even(0) == True, 'Test3'

print('OK')