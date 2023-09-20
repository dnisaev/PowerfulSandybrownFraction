def function(start, finish):
    i = start
    string = ''
    while i <= finish:      
        string = f'{string}{i}'
        i += 1            
    return string

print(function(5,10))

def function(begin, end):
    i = begin
    result = ''
    while i <= end:
        result = result + str(i)
        i += 1
    return result

print(function(3, 9))