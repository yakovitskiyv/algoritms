phrase = input().strip().split()

letters=[]
for word in phrase:
    for letter in word:
        if letter.isalpha() == True:
            letters.append(letter.lower())     

    letters_rev = list(reversed(letters))
if letters==letters_rev:
    verdict=True
else:
    verdict=False
print(verdict)