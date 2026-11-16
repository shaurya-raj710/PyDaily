# create a matrix using while loop and then find the sum of rows using for loop

row , col = map(int,input().split())

i =0
mat =[]
while(i<row):

    x = list(map(int,input().split()))

    mat.append(x)

    i+=1

print(mat)

# sum of rows

for i in range(0,row):

    sum =0

    for j in range(0,col):

        sum = sum + mat[i][j]

    print(sum, end=" ")

    
