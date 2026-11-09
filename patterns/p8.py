# hollow rectangle

row,col = map(int,input().split())
i=1
while(i<=row):

    j =1
    while(j<=col):

        if i==1 or i==row:
            print("*",end=" ")

        else:
            if j==1 or j==col:
                print("*",end=" ")

            else:
                print(" ",end=" ")

        j+=1

    print()
    i+=1