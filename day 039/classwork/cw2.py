

def full_string(list):
    full_string = ""
    i = 0
    while i <= (len(list) - 1):
        full_string += list[i]
        i += 1

    return full_string


print(full_string(["h", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d"]))