#First line n , then n lines of name score . Build a dictionary, then print the sum of all scores and the
#highest score.

n = int(input())
dict ={}
for i in range(n):
    vals = input().split()

    name = vals[0]
    marks = int(vals[1])

    dict[name] =marks


print(dict)

# sum of the marks

total = 0
highest =0

for v in dict.values():

    total = total + v

    if v > highest:
        highest =v

print(total)
print(highest)