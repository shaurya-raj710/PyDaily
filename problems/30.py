# remove the multiples

def remove(lst,k):
    n =k
    lst1 = lst
    i = len(lst) -1
    while(i>=0):
        ele = lst[i]
        if ele%n==0:
            lst.pop(i)

        i+=1

    return lst



            


arr = [3,1,2,3]
print(remove(arr,5))