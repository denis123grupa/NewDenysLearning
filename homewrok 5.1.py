
import string

value = input(str(" Enter your value in this format: a-d :"))

all_value = string.ascii_letters
string_value = ""
split_symbol = ""
joi_symbol = ""
start_symbol = ""
last_symbol = ""

split_symbol = value.split("-")
joi_symbol = "".join(split_symbol)

start_symbol = joi_symbol[0]
last_symbol = joi_symbol[1]

index_start_symbol = all_value.index(start_symbol)
index_last_symbol = all_value.index(last_symbol)

string_value = all_value[index_start_symbol:index_last_symbol + 1]

if index_start_symbol > index_last_symbol or string_value not in all_value:
    print("Not in alphabetical order")
else:
    print(string_value)