

def correct_sentence(text):
    new_text = text[0].upper() + text[1:]
    if new_text[-1] != ".":
        new_text_2 = f"{new_text}."
        return new_text_2
    else:
        return new_text

# result = correct_sentence("hello. hriends")
# print(result)


assert correct_sentence("hello, friends.") == "Hello, friends.", "Test1"
assert correct_sentence("hello") == "Hello.", "Test2"
assert correct_sentence("Hello. Friends") == "Hello. Friends.", "Test3"
assert correct_sentence("Hello, friends.") == "Hello, friends.", "Test4"
assert correct_sentence("hello, friends.") == "Hello, friends.", "Test5"
#
print("OK")
