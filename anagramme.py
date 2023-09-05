from collections import Counter

def is_anagram(str1, str2):
    
    str1 = ''.join(e for e in str1 if e.isalnum()).lower()
    str2 = ''.join(e for e in str2 if e.isalnum()).lower()
    
    
    return Counter(str1) == Counter(str2)

def main():
    input1 = input("Geben Sie den ersten Text ein: ")
    input2 = input("Geben Sie den zweiten Text ein: ")
    
    if is_anagram(input1, input2):
        print("Diese Texte sind Anagramme.🥳🎉")
    else:
        print("Diese Texte sind keine Anagramme.😱😭")

if __name__ == "__main__":
    main()
