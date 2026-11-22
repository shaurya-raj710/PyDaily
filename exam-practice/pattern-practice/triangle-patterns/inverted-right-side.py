n= int(input())

for i in range(1, n+1):

    k=1
    while(k<=(i-1)):
        print(" ", end="")

        k+=1


    for j in range(n, i-1,-1):

        if j ==i:
            print("*")


        else:
            print("*", end="")





