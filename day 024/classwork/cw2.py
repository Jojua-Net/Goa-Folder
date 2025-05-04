def clearxmovnebi(x):
    z = ("aeiou")
    j = ""
    for i in x:
        if i in z:
            continue
        else:
            j += i

    return j

print(clearxmovnebi("vaxoi"))