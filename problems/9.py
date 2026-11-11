bal = int(input())
balance = bal

decline = 0

while(bal>=0):


    x = int(input())

    if x==0:
        break
    elif x>0:
        balance = balance + x

    elif x<0:

        pos = -(x)

        if balance > pos:

            balance = balance + x

        else:

            decline = decline + 1

    if decline>=3:
        break


print(f"Final balance: {balance}")
print(f"Declined withdrawals: {decline}")
print("Session closed")
if decline>=3:
    print("Card blocked")
      

        













