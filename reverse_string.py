def function(name):
    i = 0
    string = ''
    while i < len(name):
        string = name[i] + string
        i += 1
        print(string)
    return

function("Alisa")

def function(string):
    index = len(string) - 1
    reversed_string = ''
  
    while index >= 0:
        current_char = string[index]
        reversed_string = reversed_string + current_char
        index -= 1
        print(reversed_string)
    return reversed_string

function("Hello, World!")

def function(text):
    result = ''
    for char in text:
        result = char + result      
    return result  
  
print(function("Hello"))

def to_upper(text):
    for char in text[::-1]:
        print(char.upper())

to_upper('hello')