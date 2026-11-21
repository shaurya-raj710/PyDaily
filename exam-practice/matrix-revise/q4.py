# even and odd in columns



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

    odd =0
    even =0

    row =0
    while(row<r):

        ele = mat[row][col]

        if ele%2==0:

            even = even +1

        else:

            odd +=1

        row+=1
    print(odd,even)

    col+=1



