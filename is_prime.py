def function(number):
  
    if number < 2:
        return False

    divider = 2

    while divider <= number / 2:
        
        if number % divider == 0:
          
            return False
          
        divider += 1
        print(divider)

    return True

print(function(11))