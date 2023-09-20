def function(start, end):
    i = start
    sum = i
    while i <= end:
      print(i)
      sum = sum + i
      i = i + 1
      print(sum)
    return sum

print(function(1, 10))