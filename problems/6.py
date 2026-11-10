r,c = map(int,input().split())


i=0
matA =[]
matB=[]
while(i<r):

    x = list(map(int,input().split()))


    matA.append(x)

    i+=1

j=0
while(j<r):

    y= list(map(int,input().split()))

    matB.append(y)

    j+=1


#print(matA)
#print(matB)

mat=[]
row =0

while(row<r):

    col = 0
    while(col<c):

        ele = matB[row][col] + matA[row][col]

        if col==(c-1):
            print(ele,end="")

        else:
            print(ele, end=" ")

        col+=1

    print()

    row+=1


#print(mat)

    