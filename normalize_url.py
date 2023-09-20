def function(string):
    if string[0:8] == 'https://':
        return string
    elif string[0:7] == 'http://':
        return 'https://' + string[7:]
    else:
        return 'https://' + string

string = 'http://yandex.ru'
print(function(string))

def function(text):
    return text if text[0:8] == 'https://' else 