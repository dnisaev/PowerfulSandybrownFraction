def function(string):
  match string:
    case 666: 
      return 'devil number'
    case 42:
      return 'answer for everything'
    case 7:
      return 'prime number'
    case _:
      return 'just a number'

string = 666
print(function(string))
string = 42
print(function(string))
string = 7
print(function(string))
string = 0
print(function(string))