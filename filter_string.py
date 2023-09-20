def function(text, char):
  string = ''
  
  for current_char in text:
    
    if current_char == char:
        string = '' + string
    elif current_char.lower() == char:
        string = '' + string
    elif current_char.upper() == char:
        string = '' + string
    else:
        string = string + current_char
    
    print(string)

  return string.strip()
  
text = "I look back if you are lost"
print(function(text, "I"))