depth = int(input())
up = int(input())
down = int(input())


height =0
day =0

while (height<depth):
    day = day +1

    height = height+up

    if height>=depth:
        print(f"Day {day}: Reached the top")
        break

    height = height-down
    

    print(f"Day {day}: Height = {height}")


print(f"Escaped in {day} day(s).")

