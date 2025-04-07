# 3. შექმენით manual_len ფუნქცია


def sigrdze(l):
    res = 0
    if type(l) == list:
        for z in l:
            res += 1
    elif type(l) == str or int:
        for z in str(l):
            res += 1

    return res

print(sigrdze("zd"))