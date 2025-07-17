# 1) შექმენით ფუნქცია რომელიც არგუმენტად იღებს რისცხვების ლისტს და აბრუნებტს ამ რიცხვენის ჯამს.

def x(list):
    sum_list = 0
    for i in range(0, len(list)):
        sum_list += list[i]

    return sum_list


print(x([10, 10, 10, 10, 20]))