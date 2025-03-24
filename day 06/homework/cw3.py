# 3)ამ კოდს დაამატეთ ლოგიკა, რომ 3 არასწორი პაროლის შეყვანის შემდეგ კოდი გაჩერდეს
# num = int(input("please input a number: ")) #6
# count = 0
# while num==1:
#     num=int(input("try another number: "))
# for i in range(2,num):
#     if num % i == 0 and count == 0:
#         print('Your number is not a prime')
#         count += 1
# if count == 0:
#     print('your number is a prime')



# esaa davaleba 3-is gaketeba :)


mcdeloba = 0

while mcdeloba < 3:
    num = int(input("please input a number: ")) #6
    count = 0

    if num == 1:
        print("1 არ არის მარტივი რიცხვი. სცადეთ სხვა რიცხვი.")
        mcdeloba += 1
        continue

    for i in range(2, num):
        if num % i == 0:
            print('Your number is not a prime')
            count += 1
            break
    
    if count == 0:
        print('your number is a prime')
        break

    mcdeloba += 1

if mcdeloba == 3:
    print("3 არასწორი მცდელობა იყო მეტი შანსი არ გაქვთ :)!")
