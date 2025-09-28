# 3. მოცემულია ორი სია — იპოვე მხოლოდ 
# ის ელემენტები, რომლებიც ორივე სიაშია.


l1 = [5, 10, 20, 30]

l2 = [20, 10, 5, 6, 7, 9]

oriveshia = []

for i in range(len(l1)):
    if l1[i] in l2:
        oriveshia.append(l1[i])

print(oriveshia)



