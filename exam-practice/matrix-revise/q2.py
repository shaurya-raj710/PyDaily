r,c = map(int, input().split())

i=0
mat=[]
while(i<r):

    x = list(map(int, input().split()))

    mat.append(x)

    i+=1

print(mat)

col =0
while(col<c):

    sum =0
    row =0
    while(row<r):

        ele = mat[row][col]

        sum = sum+ele

        row+=1

    print(sum)
    col+=1