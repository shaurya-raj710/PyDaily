colors = list(map(int, input().split()))



change =0
colors.sort()
i=1
while(i<len(colors)):

        if colors[i]==colors[i-1]:

                change = change+1

        i+=1

print(change)