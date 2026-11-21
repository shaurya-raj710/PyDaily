# largest element in whole matrix

r,c = map(int, input().split())

i=0
mat=[]
while(i<r):

    x = list(map(int, input().split()))

    mat.append(x)

    i+=1

print(mat)



row =0
largest = mat[0][0]
while(row<r):

    col =0
    while(col<c):

        ele = mat[row][col]

        if ele>largest:
            largest = ele


        col+=1

    row+=1

print(largest)

