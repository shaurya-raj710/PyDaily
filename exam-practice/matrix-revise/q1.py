r,c = map(int, input().split())

i=0
mat=[]
while(i<r):

    x = list(map(int, input().split()))

    mat.append(x)

    i+=1

print(mat)

row =0
while(row<r):

    sum =0
    col=0
    while(col<c):

        ele = mat[row][col]

        sum = sum + ele

        col+=1

    print(sum)
    row+=1

