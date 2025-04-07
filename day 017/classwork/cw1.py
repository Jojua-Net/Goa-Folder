listn = [1, 2, 3, 4, 5, 6]

# print(sum(listn)) === ლისტის ჯამი
# print(max(listn)) === ლისტში ყველაზე დიდს პოულობს
# print(min(listn)) === ლისტში ყველაზე პატარას პოულობს

# listn.clear() === ყველაფერს შლის ლისტში

# copy_listn = listn.copy() === აკოპირებს მთლიან ლისტს
# print(copy_listn)

# print(listn.count(2))
# print(listn.index())
# remove()
# sort()





# count function 

# def mtvleli(rame, n):
#     count = 0

#     for i in str(rame):
#         if i != str(n):
#             continue
#         else:
#             count += 1

#     return count

# print(mtvleli(555555555, 5))











def manual_sum(n):
    res = 0
    for i in n:
        res += i
    return res

print(manual_sum(listn))