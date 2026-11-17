
arr=[3,5,65,7,43]
#arr = [4, 3 ,5 ,76,42,8,96,1]

n = len(arr)

for i in range(0,n):

    min_idx = i

    for j in range(i+1,n):

        if arr[j] < arr[min_idx]:

            min_idx = j


    arr[i], arr[min_idx] = arr[min_idx], arr[i]


print(arr)