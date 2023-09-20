def function(string, char):
    i = 0
    count = 0
    while i < len(string):
      if string[i] == char:
          count += 1
      i += 1
    return count

print(function("Hello, World!", "e"))

def function(text, char):
    sum = 0
    for current_char in text:
      if current_char.lower() == char.lower():
        sum += 1
    return sum

print(function("Hello, World!", "l"))

def sum(numbers):
    result = 0
    for num in numbers:
        result += int(num)

    return result

print(sum("12345"))