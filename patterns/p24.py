# zigzag wave

w = int(input())

for i in range(1,4):

    if i==1:
        j=0
        while(j<w):
            if j%4==0:
                print("*", end="")

            else:
                print(".", end="")

            j+=1

    elif i==2:
        j=0
        while(j<w):
            if j%2!=0:
                print("*", end="")

            else:
                print(".", end="")

            j+=1

    elif i==3:
        j=0
        while(j<w):
            if j%4==2:
                print("*", end="")
            else:
                print(".", end="")

            j+=1

    print()


        

