n = int(input())


for i in range(1, n+1):

    ele = i
    for j in range(1, i+1):

        if j ==i:
            print(ele)
        else:
            print(ele, end="")

    

