
r,c = map(int, input().split())

i =0
while(i<r):

    j=0
    while(j<c):

        if (i+j)%2==0:
            print("#",end="")

        else:
            print(".",end="")

        j+=1

    print()
    i+=1
