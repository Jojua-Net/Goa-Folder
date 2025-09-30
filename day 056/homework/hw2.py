


# 2) დაწერე პროგრამა, რომელიც სიიდან გამოიტანს
# მხოლოდ იმ რიცხვებს, რომლებიც უნიკალურია (არ მეორდება).
# მაგალითი: [1,2,2,3,4,4,5] → [1,3,5]


my_list = [1,2,2,3,4,4,5]

new_list = []

for i in my_list:
    if my_list.count(i) == 1:
        new_list.append(i)


print(new_list)

# print(my_dict)