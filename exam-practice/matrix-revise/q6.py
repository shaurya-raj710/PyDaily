n = int(input())

i=1
while(i<=5):

    j =1
    while(j<=5):
        

        if i ==j or i+j ==6:

            print("*", end="")

        else:
            print(" ",end="")

        j+=1
    print()
    i+=1