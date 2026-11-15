r,c = map(int,input().split())

i =0
mat =[]
while(i<r):

    x = list(map(int,input().split()))

    mat.append(x)

    i+=1

#print(mat)

#row and col...
# if row ==0 or row == r-1 , then we have to consider the full row..
#other wise just take the j==0 and j== c-1 elements and add them

row =0
sum =0
trash =0
while(row<r):

    if row == 0 or row == (r-1):
        col = 0
        while(col<c):
            ele = mat[row][col]
            sum = sum + ele

            col+=1

    else:
        col = 0
        while (col<c):
            if col==0 or col==(c-1):

                ele = mat[row][col]

                sum = sum + ele

            col+=1

    row+=1

print(sum)


