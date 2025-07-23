

def list_sum(list):
    sum = 0
    i = 0
    while i <= (len(list) - 1):
        sum += list[i]
        i += 1
    return sum

print(list_sum([15, 20, 30, 40, 50, 60]))