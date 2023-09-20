from is_vowel.symbols import is_vowel

def count_vowels(word):
    count = 0
    for char in word:
        if is_vowel(char) == True:
            count += 1
    return count

word = "Hello, World!"

print(count_vowels(word))