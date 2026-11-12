n = int(input())

prev_row = []
i = 1

while i <= n:
    curr_row = []
    j = 1
    
    while j <= i:
        if j == 1 or j == i:
            curr_row.append(1)
        else:
            val = prev_row[j - 2] + prev_row[j - 1]
            curr_row.append(val)
        j += 1
        
    k = 1
    while k <= i:
        if k == i:
            print(curr_row[k - 1])
        else:
            print(curr_row[k - 1], end=" ")
        k += 1
        
    prev_row = curr_row
    i += 1
