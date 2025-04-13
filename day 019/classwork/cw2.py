# davaleba 2
l1 = [1, 2, 3]
l2 = [4, 5, 6]

l3 = []

for i in l1:
    l3.append(i)
l3 += l2

print(l3)