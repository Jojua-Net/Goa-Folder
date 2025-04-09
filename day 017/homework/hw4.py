# 4. შექმენით manual_pop ფუნქცია

listn = [1, 2, 3, 4, 5, 6, "ვახო", "ზდაროვა", "გელა"] # index = 8 # jami = 9

def manual_pop(l, li):
    index = li+1
    new_listn = []
    
    z = 0
        
    for i in listn:
        z+=1
        if z != index:
            new_listn.append(i)
        
        
    return new_listn
    
print(manual_pop(listn, 8))
