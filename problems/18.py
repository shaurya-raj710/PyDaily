n = int(input())

if n == 0:
    print(n)

else:

    new = n
    steps = 0

    while (new>0):

        if new%2==0:
            new = new//2
            steps+=1

        elif new%2!=0:
             new = new -1
             steps+=1

    print(steps)