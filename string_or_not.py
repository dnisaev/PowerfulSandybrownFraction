def function(string):
    return isinstance(string, str) == True and 'yes' or 'no'

string = ''
print(function(string))

string = 10
print(function(string))