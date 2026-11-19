# right pascal triangle

n = int(input())

for i in range(1,n+1):

    j =1
    while(j<=i):
        print(j, end="")

        j+=1
    print()

k = n-1

while(k>=1):

    h = 1
    while(h<=k):

        print(h,end="")
        h+=1

    print()
    k = k-1









