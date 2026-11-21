n = int(input())

for i in range(1,n+1):

    ele =i
    k=1
    while(k<=i):

        if k==i:
            print(ele)
        else:
            print(ele, end="")

        k+=1

for j in range(n-1,0, -1):

    ele =j
    d =1
    while(d<=j):
        if d==j:
            print(ele)
        else:
            print(ele, end="")

        d+=1

    

