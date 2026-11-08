# Write your reference solution here


#  6 15 24
#  12 15 18

# sum should be like this ... each row sum sone by one and in next line ... each col sum one by one \

#create matrix

row , col = map(int, input().split())

matrix = []

i = 0
while (i < row):

    x = list(map(int, input().split()))

    matrix.append(x)

    i+=1

#print(matrix)

# rows sum... rows remains constant while the val of col chnages


i = 0                  #for row
while (i < row):

    row_sum = 0                       # defined inside because it needs to restart from 0 for every row

    j = 0              # for col
    while ( j < col):

        row_sum = row_sum + matrix[i][j]


        j += 1

    if i == (row-1):

        print(row_sum, end="")                 #so that space doesnt comes after the last element

    else:
        print(row_sum, end=" ")

    i += 1

print()             # to separate the lines

# for col

j = 0


while ( j < col):

    col_sum = 0

    i = 0
    while (i < row):

        col_sum = col_sum + matrix[i][j]

        i+=1

    if j == (col - 1):

        print(col_sum, end="")

    else:
        print(col_sum, end=" ")

    j+=1

