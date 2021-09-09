lenght = input()
phrase = input().split()
max_lenght = 0
max_word = ''

for word in phrase:
    if len(word) > max_lenght:
        max_lenght= len(word)
        max_word = word

print(max_word)   
print(max_lenght)
     