# return the reverse of a number

def reverse_digits(n):
        #write code here

        n_str = str(n)
        new = n_str[::-1]
        num = int(new)

        return num