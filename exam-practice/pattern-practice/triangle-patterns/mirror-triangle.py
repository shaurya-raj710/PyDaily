# mirror triangle

n = int(input())
i =1
while(i<=n):

    j =1
    while(j<=(n-i)):
        print(" ", end="")

        j+=1

    k =1
    while(k<=i):
        print(k, end="")

        k+=1

    h = i-1
    while(h>0):
        print(h, end="")
        h-=1

    print()    
    i+=1