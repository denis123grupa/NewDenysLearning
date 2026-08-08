

###### 1 method  #######


# name = input(str("Enter the variable name:"))
#
# import string
# import keyword
#
#
# if name[0].isdigit():
#         print("Eror, starts with a digit ")
#
# for new_name in name:
#     if new_name.isupper():
#         print("Eror, contains uppercase letters.")
#         break
#
# for old_name in name:
#     if old_name in string.punctuation and old_name != "_":
#         print("Eror, is punctuation marks")
#     if old_name.isspace():
#         print("Eror, is space")
#         break
#
# if name in keyword.kwlist:
#     print("The name is in the list of reserved keywords")




###### 2 method #######



name = input(str("Enter the variable name:"))
result = True

import string
import keyword


if name[0].isdigit():
    result = False
for letter in name:
    if letter.isupper():
        result = False
if name in keyword.kwlist:
    result = False
for old_name in name:
    if old_name in string.punctuation and old_name != "_":
        result = False
for young_name in name:
    if young_name.isspace():
        result = False

print(result)



