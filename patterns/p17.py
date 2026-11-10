#right angle triangl with numbers in special pattern

n = int(input())

i=1
while(i<=n):

    j=1
    count =1
    while(j<=i):
        print(count,end=" ")

        count+=1
        j+=1

    print()
    i+=1