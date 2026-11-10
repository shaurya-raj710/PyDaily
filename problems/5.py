n = int(input())

val = "symmetric"

i= 0
mat=[]
while (i<n):

    x= list(map(int,input().split()))

    mat.append(x)

    i+=1

print(mat)

row =0
while(row<n):
    col = 0

    while(col<n):

        if mat[row][col] == mat[col][row]:
            val = "Symmetric"

        else:
            val = "Unsymmetric"

        col+=1

    row+=1

print(val)

