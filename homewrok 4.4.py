

original_name = input(str("Enter the name:"))
count = []
count_2 = []
value_1 = []
value_2 = []
encrypted_name = ""
decrypted_name = ""



for x in original_name:
    count = ord(x) + 3
    count_2 = chr(count)
    encrypted_name += str(count_2)

print(encrypted_name)

for y in encrypted_name:
    value_1 = ord(y) - 3
    value_2 = chr(value_1)
    decrypted_name += str(value_2)


print(decrypted_name)
