n = int(input())

i =1
while(i<=n):

    j =1
    while(j<=(n-i)):
        print(" ", end="")

        j+=1

    m =1
    while(m<=i):
        print(chr(65+m-1), end="")
        m+=1

    k =i-1
    while(k>0):
        print(chr(65+k-1), end="")
        k-=1


    print()
    i+=1