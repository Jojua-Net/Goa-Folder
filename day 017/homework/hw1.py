# 1. შექმენით manual_remove ფუნქცია

listn = [1, 2, 3, 4, 5, 6]
def manual_remove(l, li):
    new_listn = []
    for i in l:
        if i != li:
            new_listn.append(i)
    return new_listn

print(manual_remove(listn, 5))