n = int(input())

for i in range(1, n+1):

    j =1 
    while(j<=(i-1)):

        print(" ", end="")

        j+=1


    k=1
    while(k<=(n-i+1)):

        if k==(n-i+1):
            print("*")
        else:
            print("*", end="")


        k+=1

    




 