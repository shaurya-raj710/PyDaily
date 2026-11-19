#mirror number triangle ...

n = int(input())

i =1
while(i<=n):

    for j in range(1,i+1):
        print(j, end="")


    for k in range(2*n-2*i,0,-1):
        print(" ", end="")

    p = i
    
    while(p>=1):
        print(p, end="")

        p =p-1





    print()
    i+=1

i =n

