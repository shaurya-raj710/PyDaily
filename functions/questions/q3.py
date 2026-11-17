#Middle Item of Anything

def middle_item(seq):
    """Return the middle item of seq."""
    # your code here

    m = len(seq)
    n = m-1
    mid = 0
    if (n)%2!=0:
        mid = mid + n//2

    else:
        mid = n//2

    ele = seq[mid]
    return ele