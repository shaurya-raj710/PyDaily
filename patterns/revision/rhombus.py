# revising the pattern of solid rhombus

r,c = map(int, input().split())

row=1
while (row<=r):

    col =1
    while(col<=(c-row)):
        print(" ",end="")

        col+=1

    m=1
    while(m<=c):
        print("*", end="")

        m+=1

    print()
    row+=1




