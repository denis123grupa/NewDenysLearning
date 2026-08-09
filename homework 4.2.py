


first_adress = input(str("Enter the variable name:"))

result = ""
hashtag = '#'
new_result = []



import string


for x in first_adress:
    if x not in string.punctuation:
        result += x

result = result.split(" ")
for a in result:
    new_result.append(a.capitalize())
result = "".join(new_result)

result = f"{hashtag}{result}"

if len(result) > 140:
    result = result[:140]


print(result)




