#hollow equilateral triangle

n = 5

i=1
while(i<=n):

    j=1
    while(j<=(n-i)):
        print(" ",end="")

        j+=1

    if (i==1 or i==n):
        x=1
        while(x<=(2*i-1)):
            print("*", end="")

            x+=1

    else:
        print("*",end="")
        k= 1
        while(k<=(2*i-3)):
            print(" ",end="")
            k+=1

        print("*",end="")

    print()
    i+=1

