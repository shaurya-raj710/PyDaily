#equilateral triangle with some number pattern

n = 9

i =1
while(i<=n):

    j=1
    while(j<=(n-i)):
        print(" ",end=" ")

        j+=1

    m =1
    count =1
    while(m<=i):
        print(count,end=" ")

        count+=1
        m+=1

    x=i-1
    while(x>=1):
        print(x,end=" ")
        x =x-1

    print()
    i+=1