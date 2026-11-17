
# museum ticket price


def ticket_price(age, day="weekday", member=False):

        price =0
        dist =0
        add =0
        if age<5:
                return 0                         # here i did a small mistake tbh
                                                  # the code is mow correct

        if age>=5 and age <=59:
                price = 200
        elif age >=60:
                price = 120

        if day =="weekend":
                add =50
        else:
                add = 0

        if member==True:
                dist = -30

        else:
                dist =0
        
        total = price + add + dist

        return total