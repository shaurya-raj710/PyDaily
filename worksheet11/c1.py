#For every number from 1 to n , print Fizz if it is divisible by 3, 
# Buzz if by 5, FizzBuzz if by both,
#otherwise the number itself — one per line.


n = int(input())

i=1
while(i<=n):

    if (i%3==0 and i%5==0):
        print("FizzBuzz")

    elif (i%3==0):
        print("Fizz")

    elif (i%5==0):
        print("Buzz")

    else:
        print(i)

    i+=1