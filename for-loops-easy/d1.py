# generate a multiplication table

n,limit = map(int, input().split())

for i in range(1,limit+1):
    mul = i*n
    print(f"{n} x {i} = {mul}")