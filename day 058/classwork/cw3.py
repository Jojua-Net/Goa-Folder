# 3 classwork
def userinfo(name, age, favcolor):
    mydictt = {
        "name": name,
        "age": age,
        "favcolor": favcolor,
    }
    
    for i in mydictt.values():
        print(i)

    return mydictt
    
    
print(userinfo("vaxo", 16, "orange"))