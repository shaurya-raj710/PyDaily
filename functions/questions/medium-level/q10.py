# create a function to print the sum of its digits

def length(n):

    str_n = str(n)
    new = str_n[::-1]

    num = int(new)

    return num

print(length(2100))

