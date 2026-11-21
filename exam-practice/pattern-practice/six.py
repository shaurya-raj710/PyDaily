n = int(input())

for i in range (1,n+1):

    for j in range(n-i):
        print(" ", end="")

    k =1
    m =i
    while(k<=(2*i)-1):

        if k==((2*i)-1):
            print("*")

        else:
            print("*", end="")

        k+=1

