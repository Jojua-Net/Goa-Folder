# davaleba 1

def func(mylist, n):
    res = []
    for i in mylist:
        if i % n == 0:
            res.append(i)

    return res

print(func([1,23,165,2,3,92,10,34,911], 3))