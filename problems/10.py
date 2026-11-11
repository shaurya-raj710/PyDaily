n = int(input())
steps = 0

while n >= 10:
    old_n = n
    total = 0
    

    while n > 0:
        last_digit = n % 10       
        total = total + last_digit
        n = n // 10               
        
    n = total
    steps = steps + 1
    print(old_n, "->", n)

print("Single digit:", n)
print("Steps:", steps)
