#solid equilateral triangle

n = 5

i = 1
while(i<=n):

    j = 1
    while(j<=(n-i)):
        print(" ",end="")

        j+=1

    x = 1
    while(x<=(2*i-1)):
        print("*", end="")

        x+=1

    print()
    i+=1
