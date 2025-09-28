# 1. მოცემულია რიცხვების სია — 
# იპოვე და დაბეჭდე ის რიცხვები, რომლებიც სიაში მეორდება.


mylist = [10, 10, 5, 6, 8, 8, 12, 12, 9, 3, 2, 1, 0, 0]

repeated = []

for i in range(len(mylist)):
    for x in range(i+1, len(mylist)):
        if mylist[i] == mylist[x] and mylist[i] not in repeated:
            repeated.append(mylist[i])
        
    
print(repeated)

    