#solid diamond pattern

n =4

i=1
while(i<=n):

    j=1
    while(j<=(n-i)):
        print("#",end="")

        j+=1

    x =1
    while(x<=(2*i-1)):
        print("*",end="")

        x+=1

    #now inverted

 

    print()




    i+=1

i = 1
while(i<=n):

    j=1
    while(j<i):
        print("#",end="")

        j+=1

    print()
    i+=1