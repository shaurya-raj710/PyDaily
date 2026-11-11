r,c = map(int,input().split())

i=0
mat =[]
while(i<r):

    x= list(map(int, input().split()))

    mat.append(x)

    i+=1

print(mat)

largest = mat[0][0]
rowl=0
coll=0
#print(largest)

i =0

while(i<r):

    j=0

    while(j<c):

        ele = mat[i][j]

        if ele > largest:

            largest = ele
            rowl = i
            coll = j

        j+=1

    i+=1

print(f"{largest} {rowl} {coll}")