# equilateral triangle with special number pattern

n = int(input())
i=1
count =1

while(i<=n):

    j=1
    while(j<=(n-i)):
        print(" ",end=" ")
        j+=1

    x=1
    while(x<=i):
        print(count,end=" ")

        x+=1

    m=2
    while(m<=i):
        print(count,end=" ")
        m+=1

    print()
    count+=1
    i+=1