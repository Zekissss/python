def is_palindrome(text):
    text = text.lower()
    cleaned_text = ''.join(e for e in text if e.isalnum())
    return cleaned_text == cleaned_text[::-1] if cleaned_text else False

user_input = input("Einen Text eingeben: ")

if is_palindrome(user_input):
    print("Das ist ein Palindrom.😁")
else:
    print("Das ist kein Palindrom.😟")
