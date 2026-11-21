r,c = map(int, input().split())

i=0
mat=[]
while(i<r):

    x = list(map(int, input().split()))

    mat.append(x)

    i+=1

print(mat)

# largest element in each row

row =0
while(row<r):

    largest = mat[0][0]

    col = 0

    while(col<c):

        ele = mat[row][col]

        if ele>largest:
            largest = ele

        col+=1

    print(largest)
    row+=1