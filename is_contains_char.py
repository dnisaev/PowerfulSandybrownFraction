def function(word, char):
  
  i = 0
  
  while i < len(word):

    word_upper = word.upper()
    word_lower = word.lower()
    
    if word[i] == char:
      return True      
    elif word_upper[i] == char:
      return True     
    elif word_lower[i] == char:
      return True
    i += 1
  
  return False

print(function("Hexlet", "h"))