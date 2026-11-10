r , c ,k = map(int,input().split())

i=0
mat =[]
while(i<r):

    x=list(map(int,input().split()))

    mat.append(x)

    i+=1

print(mat)

row =0
div =0
while(row<r):
    col = 0

    while(col<c):

        ele = mat[row][col]

        if ele%k ==0:
            div = div +1


        col+=1
    row+=1

print(div)

