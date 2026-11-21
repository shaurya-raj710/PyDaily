n = int(input())

for i in range(1, n+1):

    j=1
    while(j<=i):

        if j==i:
            print(j)

        else:
            print(j, end="")

        j+=1

    i+=1