text = 'Hello, World!'

def function(text, offset=0, repetitions=1):

    return text[offset:] * repetitions

print(function(text, 7, 3))