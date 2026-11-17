#Grade Letter with a Pass Mark



def grade_letter(score, pass_mark=40):
    # Write your reference solution here

    if score >=90:
        return "A"

    elif score >=75:
        return "B"

    elif score >= 60:
        return "C"

    elif score>=pass_mark :
        return "D"

    else:
        return "F"