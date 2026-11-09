#solid rectangular pattern

row , col = map(int, input().split())

i = 0

while(i <row):

    j = 0
    while (j < col):

        print("*", end=" ")

        j +=1

    print()
    i+=1