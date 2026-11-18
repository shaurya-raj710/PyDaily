# create a function which takes a list and then returns its maximum value

def max(arr):

    maxi = arr[0]
    for i in arr:
        if i> maxi:
            maxi = i

    return maxi

arr = [3,5,8,21,3,9,2]

print(max(arr))