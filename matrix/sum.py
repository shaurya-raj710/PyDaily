# sum of all elements of a matrix

row , col = map(int, input().split())

i = 0
matrix = []
while (i < row):

    x = list(map(int, input().split()))

    matrix.append(x)

    i+=1

print(matrix)

# for sum

sum = 0
i = 0            # for row

while(i < row):

    j = 0         #for elemets of col (0 to n-1)

    while (j< col):

        sum = sum + matrix[i][j]


        j += 1

    i += 1


print(sum)
