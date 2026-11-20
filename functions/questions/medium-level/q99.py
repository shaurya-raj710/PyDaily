# create a function in which you sort the array in ascending order 

def sortN(arr):

    n = len(arr)
    i =1
    while(i<n):

        key = arr[i]
        j = i-1

        while j>=0 and arr[j]> key:

            arr[j+1] =arr[j]
            j-=1

        arr[j+1] = key
        i+=1

    return arr

print(sortN([34,54,3,4,87,42]))