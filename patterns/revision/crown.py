n = int(input())

i=1
while(i<=n):

    j=1
    while(j<=i):

        print("*", end="")

        j+=1

    k =1
    while(k<=(n-i)):
        print(" ", end="")
        k+=1

    l =1
    while(l<=(n-i)):
        print(" ", end="")
        l+=1

    m =1
    while(m<=i):
        print("*", end="")

        m+=1
    print()
    i+=1