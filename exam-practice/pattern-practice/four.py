n = int(input())

for i in range(1,n+1):

    j =1
    while(j<=(n-i)):

        print(" ", end="")

        j+=1

    k =1
    while(k<=i):

        if k==i:
            print("*")

        else:
            print("*", end="")

        k+=1



