r,c,k = map(int,input().split())

i =0
mat =[]
while (i<(r*c)):

    temp = list(map(int, input().split()))

    mat.append(temp)

    i+=1

print(mat)

sum = 0
k=0
while (k<r):

    
    j =0
    while(j<c):

        ele = mat[k][j]

        sum +=ele

        j+=1


    m = 0
    while(m<k)

    k+=1




print(sum)



