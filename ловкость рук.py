from collections import Counter

k = int(input()) * 2
mat = []
for i in range(4):
    numbers = input()
    mat += numbers

max_score = sum(1 for key, value in Counter(mat).items() if key.isdigit() and value <=k)

print(max_score)

"""
print(sum(                                    
    1                                           
    for key, value in Counter(            
        count for _ in range(4) for count in input()
    ).items()    
    if key.isdigit() and value <= k
    )
)

"""
