n = int(input())

vals = (input().split())
sets = set()

for i in range(n):

    ele = int(vals[i])
    sets.add(ele)
print(len(sets))