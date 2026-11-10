#crown

n = int(input())

i =1
while(i<=n):

    j=1
    while(j<=i):
        print("*",end="")
        j+=1

    x=1
    while(x<=(n-i)*2):
        print(" ",end="")

        x+=1

    m =1
    while(m<=i):
        print("*",end="")

        m+=1

    print()
    i+=1

#below part

i=1
while(i<=n):

    j=1
    while(j<=(n+1-i)):
        print("*",end="")
        j+=1


    x=1
    while x<=(2*i-2):
        print(" ", end="")
        x+=1

    m=1
    while(m<=(n+1-i)):
        print("*",end="")

        m+=1




    print()
    i+=1