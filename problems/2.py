# taking input

goal = int(input())

total_days = 0
goals_met = 0

best_day = 0
best_day_steps =0

while True():

    steps = int(input())

    

    if steps == -1:
        break

    else:



        

        if steps >= goal:
            goals_met = goals_met + 1
            total_days +=1

            

            print(f"Day {total_days}: {steps} - Goal met")


        else :

            total_days = total_days + 1
            print(f"Day {total_days}: {steps} - Goal missed")



    