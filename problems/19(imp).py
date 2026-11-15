n = int(input())

uniq = set()

i=0
while(i<n):

    x,y = map(int, input().split())

    point = (x,y)  #tuple

    uniq.add(point) # tuple inside set

    i+=1
#prinitng len of set

print(len(uniq))

sorted_coords = sorted(uniq)

j=0
while(j<len(sorted_coords)):

    point = sorted_coords[j]
    print(point[0], point[1])


    j+=1

