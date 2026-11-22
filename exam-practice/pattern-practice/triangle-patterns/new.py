n = 3

i = 0
while i < n:
    print("  " * (n - i - 1), end="")

    j = 1
    while j <= i + 1:
        print(j, end=" ")
        j += 1

    j = i
    while j >= 1:
        print(j, end=" ")
        j -= 1

    print()
    i += 1