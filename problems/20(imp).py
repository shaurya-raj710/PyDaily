n = int(input())

banned = set(input().split())

q = int(input())

names = input().split()

#print(type(names))

i=0
while(i<q):
    username = names[i]

    if username in banned:
        print("BANNED")

    else:
        print("OK")

    i+=1

