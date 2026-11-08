# transpose of a matrix

# create

row , col = map(int, input().split())

i = 0
matrix = []
while ( i < row):

    x = list(map(int, input().split()))

    matrix.append(x)

    i+=1

#print(matrix)

# now transpose.... row to col and col to row

j = 0

new_mat =[]

while ( j < col):

    temp =[]

    i = 0
    while (i < row):

        if (i == row-1):

            print(matrix[i][j], end="")

        else:
            print(matrix[i][j],end=" ")

        

        i+=1
    print()

    j+=1



    

