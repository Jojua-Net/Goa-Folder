# ინტერვიუს classwork-ი #1

def palidrome(x):
    if x == x[::-1]:
        return True
    else:
        return False

print(palidrome("ana")) 

def palidrome2(x2):
    return True if x2 == x2[::-1] else False

print(palidrome2("giorgi"))