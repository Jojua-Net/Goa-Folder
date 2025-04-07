# 4. შექმენით manual_pop ფუნქცია

listn = [1, 2, 3, 4, 5, 6]

def manual_pop(l, li):
    count = 0
    lindex = l.index(li)
    for i in l:
        count += 1
        if lindex == li:
            break
        
    return count 


print(manual_pop(listn, 2))