##### option 1 ######

# def is_even(value):
#
#     if not str(value).strip("-").isdigit():
#
#         return "Sorry, the value is not a digit"
#
#     if (str(value).endswith("0")
#
#     or str(value).endswith("2")
#
#     or str(value).endswith("4")
#
#     or str(value).endswith("6")
#
#     or str(value).endswith("8")):
#
#         return True
#
#     else:
#
#         return  False
#
# print(is_even(5689))
#
# assert is_even(2) == True, 'Test1'
#
# assert is_even(5) == False, 'Test2'
#
# assert is_even(0) == True, 'Test3'
#
# print('OK')

# #### option 2 #####
#
# def is_even(value):
#
#     if not str(value).strip("-").isdigit():
#
#         return "Sorry, the value is not a digit"
#
#     if (str(value)[-1] == "0"
#
#     or str(value)[-1] == "2"
#
#     or str(value)[-1] == "4"
#
#     or str(value)[-1] == "6"
#
#     or str(value)[-1] == "8"
#
#     ):
#
#         return True
#
#     else:
#
#         return  False
#
# print(is_even(5689))
#
# assert is_even(2) == True, 'Test1'
#
# assert is_even(5) == False, 'Test2'
#
# assert is_even(0) == True, 'Test3'
#
# print('OK')

#### option 3 ####

def is_even(value):

    if not str(value).strip("-").isdigit():

        return "Sorry, the value is not a digit"

    if str(value)[-1] in "02468":

        return True

    else:

        return  False

print(is_even(5689))

assert is_even(2) == True, 'Test1'

assert is_even(5) == False, 'Test2'

assert is_even(0) == True, 'Test3'

print('OK')