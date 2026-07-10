numbers = ["Hello", "Denys", True, 1]
summ_meaning = len(numbers)

if summ_meaning == 0:
    print(numbers)
elif summ_meaning % 2 == 0:
    result = summ_meaning // 2
    first_part = numbers[:result]
    second_part = numbers[result:]
    result_2 = [first_part,  second_part]
    print(result_2)
elif summ_meaning % 2 > 0:
    result = summ_meaning // 2
    first_part = numbers[:result]
    second_part = numbers[result:]
    result_2 = [first_part, second_part]
    print(result_2)
    a