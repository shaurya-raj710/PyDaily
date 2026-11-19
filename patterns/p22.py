#hollow rigth triangle

n = int(input())

i=1
while(i<=n):

    if(i==1 or i==2 or i==n):

        j=1
        while(j<=i):
            print("*", end="")

            j+=1

    else:

        print("*", end="")
        k=1
        while(k<=(i-2)):

            print(" ", end="")

            k+=1

        print("*", end="")

    print()
    i+=1