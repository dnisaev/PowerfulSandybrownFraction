from random import randint

def choise_from_range(word, begin_num, end_num):

    random_char = randint(begin_num, end_num)

    return word[random_char]

print(choise_from_range("Alisa and Polina", 0, 10))