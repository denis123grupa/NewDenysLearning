numbers = ["How are you ?", "By", "Hello"]

if len(numbers) <= 1:
    print(numbers)

elif len(numbers) >= 1:
    numbers_1 = numbers[-1]
    numbers.insert(0, numbers_1)
    numbers.pop()
    print(numbers)
