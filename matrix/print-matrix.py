# read the matrix and then print it as it is
# the last element of each row must not have spaces at the end

r,c = map(int, input().split())

i =0
mat=[]
while(i<r):

    x = list(map(int, input().split()))

    mat.append(x)

    i+=1

print(mat)

# now the matrix has been made

for i in range(r):

    j=0
    while(j<c):

        ele = mat[i][j]

        if j==(c-1):
            print(ele)
        else:
            print(ele, end=" ")

        j+=1

    