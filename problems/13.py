n = int(input())

i = 1
while i <= n:
    j = 1
    
    while j <= n:
        if i > j:
            val = i
        else:
            val = j
            
        if j == n:
            print(val)
        else:
            print(val, end=" ")
            
        j += 1
    i += 1