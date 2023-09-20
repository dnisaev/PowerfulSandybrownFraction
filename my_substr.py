def function(string, char):
    i = 0
    result = ''    
    while i < char:
        result = result + string[i]
        i += 1
        print(result)
    return result

function("Hello, World!", 1)  