words = list(input().split())
print(words)

i=0
great_index=0
g_word = ""

while(i<len(words)):

    if len(words[i])>len(g_word):
        g_word = words[i]

    i+=1

print(g_word)