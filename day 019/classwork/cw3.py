# davaleba 3
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def func(l):
    l2 = []
    for i in l:
        if i % 2 != 0:
            continue
        else: l2.append(i)

    return l2

print(func(l1))