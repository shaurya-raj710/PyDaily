seat = int(input())
slot = int(input())
student = int(input())
price = 0

if seat == 1:

    if slot ==1:
        price = 100

    elif slot == 2:
        price =120

    else:
        price = 150

elif seat == 2:
    if slot == 1:
        price = 150

    elif slot == 2:
        price = 180

    else :
        price = 220

elif seat == 3:

    if slot == 3:
        price = 300

    else :
        price = 250

final = price

if student == 1:

    if slot ==1 or slot ==2:

        final = price - 30

print(price)
print(final)