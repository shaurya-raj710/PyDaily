s = input().strip()


char_set = set(s)
#print(char_set)

num =0
for i in char_set:

        num = num + 1

#print(num)

if num%2==0:
        print("CHAT WITH HER!")

else:
        print("IGNORE HIM!")