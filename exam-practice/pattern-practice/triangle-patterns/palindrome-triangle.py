# palindrome triangle

n = int(input())

i =1
while(i<=n):

    for j in range(n-i):
        print(" ", end="")

    k=i
    while(k>=1):
        print(k, end="")
        k=k-1

    m =1
    while(m<=i-1):
        print(m+1, end="")
        m+=1
    print()
    i+=1