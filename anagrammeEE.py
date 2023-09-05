def main():
    input1 = input("Geben Sie den ersten Text ein: ")
    input2 = input("Geben Sie den zweiten Text ein: ")

    cleaned_str1 = ""
    for char in input1:
        if char.isalnum():  
            cleaned_str1 += char

    cleaned_str2 = ""
    for char in input2:
        if char.isalnum():
            cleaned_str2 += char

    if sorted(cleaned_str1) == sorted(cleaned_str2):
        print("Diese Texte sind Anagramme.🥳🎉")
    else:
        print("Diese Texte sind keine Anagramme.😱😭")

if __name__ == "__main__":
    main()
