# plus sign

#print((7+1)//2)

n = int(input())
i=1
while(i<=n):

    mid = (n+1)//2

    if(i==mid):
        for k in range(1,6):

            print("*", end="")

    else:

             

        j=1
        while(j<=n):

            

            

            if (j==mid):
                print("*", end="")

            else:
                print(".", end="")


            j+=1
    print()
    i+=1

        