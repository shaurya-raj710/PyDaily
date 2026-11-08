# creating a matrix

row , col = map(int, input().split())

i = 0
mat = []

while ( i < row):

    
    x = list(map(int, input().split()))

    mat.append(x)

    i+=1

print(mat)


