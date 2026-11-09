#solid rhombus

n = int(input())

i =1
while(i<=n):

    j = 0
    while(j< (n-i)):
        print(" ",end="")

        j+=1

    x = 1
    while(x<=n):
        print("*",end="")

        x+=1


    print()
    i+=1