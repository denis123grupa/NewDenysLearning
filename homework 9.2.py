


#### option 1 ######

def first_word(text):
    def letters_and_spaces():
        first_text = ""
        for value in text:
            if value.isalpha() or value == "'" or value.isspace():
                first_text += value
            else: first_text += " "

        return first_text

    def list_without_spaces():
        new_text = result.strip().split()
        return new_text[0]

    result = letters_and_spaces()
    word = list_without_spaces()
    return word

print(first_word( " ,. 2 don't. tuch  "))

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'



