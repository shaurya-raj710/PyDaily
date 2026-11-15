n = int(input())
str_n = str(n)
i=0
digit =0
while(i<len(str_n)):

    last = n%10
    dig = (last)*2**i

    n = n//10

    digit = digit+dig

    i+=1

print(digit)

