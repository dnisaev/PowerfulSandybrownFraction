def function(string):
    last_char = string[-1]
    if last_char == '?':      
        sentence_type = 'question'      
    elif last_char == '!':
        sentence_type = 'exclamation'
    else:            
        sentence_type = 'normal'
    return "Sentence is " + sentence_type

string = 'Hello, World!'
print(function(string))

string = 'Hello, World?'
print(function(string))

string = 'Hello, World'
print(function(string))

def function(text):
    return 'question' if text[-1] == '?' else 'normal'

text = 'Hello, World!'
print(function(text))
text = 'Hello, World?'
print(function(text))