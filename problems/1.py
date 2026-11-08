zone = int(input())
w = int(input())
exp = int(input())

total = 0
base = 0
exp_charge =0

if zone == 1:

    if w <= 2:
        base = 40

    elif w <=5 :
        base = 70

    else :
        base = 100

elif zone == 2:

    if w <=1 :
        base = 60

    else :
        base = 110


elif zone == 3:

   if w <= 1:
        base= 120

   elif w<=3:
       base = 200

   elif w<=10:
       base = 350

   else:
       base = 500


if exp == 1:

    if zone == 1:
        exp_charge = 30

    elif zone == 2:
        exp_charge = 50

    elif zone == 3:
        exp_charge = 100


total = base + exp_charge
print(base)
print(total)