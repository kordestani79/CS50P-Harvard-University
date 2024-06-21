def convert_emoticons(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

user_input = input()
converted_text = convert_emoticons(user_input)
print(converted_text)
