# creating a matrix

row,col = map(int,input().split())
i=0
mat =[]
while(i<row):

    x = list(map(int,input().split()))

    mat.append(x)

    i+=1

#print(mat)

#sum of borders..
#border 1
horizontal =0
i=0
while(i<row):
    j=0
    while(j<col):
        horizontal = horizontal + mat[i][j]

        j+=1

    i = i+(row-1)

#print(horizontal)

j=0
vertical =0
while(j<col):

    i=0
    while(i<row):
        vertical = vertical + mat[i][j]

        i+=1

    j = j+(col-1)

print(horizontal +vertical)
