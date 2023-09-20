def function(word):  
    string = ''
    if word == string:
        return True

    for char in word:      
        string = char + string
        print(string)

        if string.lower() == word.lower():
          return True
      
    return False    

print(function("Tokot"))