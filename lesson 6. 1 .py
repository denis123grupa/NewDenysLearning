
first_symbol = float(input("1st num: "))
my_operator = input("operator (+, -, *, /)")
second_symbol = float(input("2nd num: "))

# if len(my_operator) > 1:
#     print("Eror")


# if my_operator != "+" or my_operator != "-" or my_operator != "*" or my_operator != "/":
# if my_operator not in "+-*/" or len(my_operator) != 1:
# if my_operator not in ["+", "-", "*", "/"]:

result = 0

if my_operator not in ("+", "-", "*", "/"):
    result = ("Eror wrong operator")

else:
    if my_operator == "+":
      result = (first_symbol + second_symbol)
    elif my_operator == "-":
      result = (first_symbol - second_symbol)
    elif my_operator == "*":
      result = (first_symbol * second_symbol)
    elif my_operator == "/":
      if second_symbol != 0:
        result = (first_symbol / second_symbol)
      elif second_symbol == 0:
        result = ("Eror - can't divide by zero")



print(result)


# else:
#     # print("Eror wrong operator")

# "Eror - can't divide by zero"