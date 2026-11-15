price = int(input())
save = int(input())
spend = int(input())

balance =0
month =0

while True:

    

    
        
        balance = balance + save


        month = month+1

        if balance>=price:
                print(f"Month {month}: Can buy the bicycle")
                break

        balance = balance - spend

        print(f"Month {month}: Balance: {balance}")



print(f"Bought in {month} month(s).")