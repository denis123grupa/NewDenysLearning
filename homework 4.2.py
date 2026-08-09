


first_adress = input(str("Enter the variable name:"))

result = ""
hashtag = '#'
new_result = []



import string

result = first_adress.split(" ")
for a in result:
    new_result.append(a.capitalize())
result = "".join(new_result)
for x in first_adress:
    if x not in string.punctuation and x == " ":
        result += x
result = f"{hashtag}{result}"




print(result)




