a = input()   
b = input()  
result = ""   
for i in range(ord(a), ord(b) + 1):
    result += chr(i)
print(result)