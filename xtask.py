def function(word):    
    
    string = ""
    sum = 1
    i = 0
     
    while i < len(word) - 1:
      
        string = f'{string}{word[i]}'
      
        print(f'''
        Символ до = {word[i]}
        Сумма до = {sum}
        Строка до = {string}''')        
      
        if word[i] == word[i + 1]:
          sum += 1

        elif word[i] != word[i + 1]:
          string = f'{string}{sum}'
          sum = 1

        print(f'''
        Символ после = {word[i]}
        Сумма после = {sum}
        Строка после = {string}''')
      
        i += 1        
      
    string = f'{string}{word[i]}{sum}'
    
    return string

word = "aabbccc"

print(function(word))