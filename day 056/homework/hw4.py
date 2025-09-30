



# 4) დაწერე პროგრამა, რომელიც სიას დაალაგებს ისე, რომ ლუწები იყოს წინ და კენტები — უკან.
# მაგალითი: [1,2,3,4,5,6] → [2,4,6,1,3,5]


my_list = [1,2,3,4,5,6]


Odd = []
Even = []


for i in range(len(my_list)):
    if my_list[i] % 2 == 0:
        Even.append(my_list[i])
    else:
        Odd.append(my_list[i])

print(Even + Odd)