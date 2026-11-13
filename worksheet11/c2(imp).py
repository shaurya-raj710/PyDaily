#Repeatedly replace n by the sum of its digits until a single digit remains.
#  Print how many times you had
#to do this (0 if n is already a single digit).

n = int(input())
steps = 0

while (n>=10):

    sum =0
    while (n>0):
        last = n%10
        sum = sum + last
        n = n//10

    n=sum
    steps +=1

print(steps)