
number = int(input('Enter your number: '))

number_1 = (number % 10 )
number_2 = (number % 100 // 10 )
number_3 = (number % 1000 // 100 )
number_4 = (number % 10000 // 1000 )
number_5 = (number // 10000 )


result_1 = (number_1 * 10000 )
result_2 = (number_2 * 1000 )
result_3 = (number_3 * 100 )
result_4 = (number_4 * 10 )
result_5 = (number_5 * 1)

print(result_1 + result_2 + result_3 + result_4 + result_5)

