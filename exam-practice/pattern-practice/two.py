n = int(input())

i =n
while(i>=1):

    j=1
    while(j<=i):

        if j==i:
            print("*")

        else:
            print("*", end="")

        j+=1
    i-=1

