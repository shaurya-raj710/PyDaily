#Read a square N × N matrix. Print the sum of the main diagonal and the sum of the anti-diagonal.

#create

row , col = map(int,input().split())

i = 0
matrix = []
while (i < row):

    x = list(map(int, input().split()))

    matrix.append(x)

    i+=1

print(matrix)

# diagonal.... ( row and col are same)

dia_sum = 0
i = 0

while ( i < row):

    dia_sum = dia_sum + matrix[i][i]

    i +=1

print(dia_sum, end=" ")

# anti - diagonal

i = 0                       # 0 to row-1
anti = 0
while ( i < row):

    anti = anti + matrix[i][row - i - 1]


    i+=1


print(anti)


