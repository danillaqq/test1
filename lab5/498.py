s = input()

num = ""     
result = ""   

for ch in s:
    if ch.isdigit():
        num = num + ch            
    else:
        if num == "":             
            result = result + ch
        else:
            result = result + ch * int(num)
        num = ""                  

print(result)