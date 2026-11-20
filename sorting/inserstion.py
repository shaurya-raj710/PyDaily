# insertion sort

arr = [34,5,65,3,2,45]

n = len(arr)

i=1
while (i<n):

    key = arr[i]
    j = i-1

    while(j>=0 and arr[j]> key):

        arr[j+1] = arr[j]
        j-=1

    arr[j+1] = key
    i+=1

print(arr)