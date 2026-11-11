n = int(input())

new =""
n_str= str(n)
leng = len(n_str)
i=0
while(i<leng):

    dig = n%10

    new = new+ str(dig)

    n = n//10

    i+=1

print(int(new))