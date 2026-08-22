
original_name = input(str(" Hi, my friend! I’ll help you encrypt the text. Please enter the name: "))



count = []
count_2 = []
value_1 = []
value_2 = []
encrypted_name = ""
decrypted_name = ""



for x in original_name:
    count = ord(x) + 100
    count_2 = chr(count)
    encrypted_name += str(count_2)
print(encrypted_name)

ok = input(str("Do you want to decrypt the name? If yes, enter yes. If not, enter no: "))

if ok == "yes":

    for y in encrypted_name:
        value_1 = ord(y) - 100
        value_2 = chr(value_1)
        decrypted_name += str(value_2)

    print(decrypted_name)
else:
    print(f" Then let’s leave it encrypted:   {encrypted_name}")

