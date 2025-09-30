


# 3) დაწერე ფუნქცია, რომელიც იღებს 
# მთელ რიცხვს და აბრუნებს მის ციფრთა ჯამს.
# მაგალითი: 1234 → 10



def number_sum(num):

    num = str(num)
    total = 0

    for i in range(len(num)):
        total += int(num[i])

        

    return total


print(number_sum(1234))
print(number_sum(15))
print(number_sum(10))