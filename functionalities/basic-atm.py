# we are going to create a atm machine using python, i mean a basic atm machine

balance =0

while True:

    print("Welocme to our Basic atm machine")
    print("1. BALANCE\n2. DEPOSIT\n3. WITHDRAW\n4. EXIT")

    val = int(input())

    if val==4 or val=="4":

        break

    elif val ==1:

        print("Balance :", balance)

    elif val == 2:

        print("enter the amt you want to deposit")

        depo = int(input())

        balance = balance+ depo

    elif val ==3:

        print("enter the amt you want to take out")

        withd = int(input())

        if balance<withd:

            print("sorry you dont have enough money")

        else :

            balance= balance - withd

        
