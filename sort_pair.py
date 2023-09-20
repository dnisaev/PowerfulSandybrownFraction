def function(sort):
  
    first, second = sort
  
    if first <= second:
      return first, second
    return second, first


sort = (15, 10)
print(function(sort))