# right angled triangle of numbers with progression

n = int(input())
count = 1

i =1
while(i<=n):

    j=1
    while(j<=i):
        print(count,end=" ")

        j+=1
        count+=1

    print()
    i+=1