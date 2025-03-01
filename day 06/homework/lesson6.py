# 1) მომხმარებელს შემოატანინეთ რიცხვი, შემდეგ for ციკლის გამოყენებით, 
# გამოთვალეთ და გამოიტანეთ მხოლოდ კენტი რიცხვების ჯამი


# user_num = int(input("Enter Number: "))
# jami = 0
# for i in range(1, user_num):
#     if i % 2 == 1:
#         print("ესაა რიცხვები რომლებიც შეკრიბეთ: ", i)
#         jami += i

# print("ჯამი:", jami)




# 2)მომხმარებელს შემოატანინეთ რიცხვი, შემდეგ for ციკლის გამოყენებით გამოიტანეთ მხოლოდ 
# ის რიცხვები, რომლებზეც უნაშთოდ იყოფა შემოტანილი რიცხვი

# user_num = int(input("Enter Number: "))

# for i in range(1, user_num):
#     if user_num % i == 0:
#         print("რიცხვი რომელიც იყოფა", user_num, "-ზე არის:", i)






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


# mcdeloba = 0

# while mcdeloba < 3:
#     num = int(input("please input a number: ")) #6
#     count = 0

#     if num == 1:
#         print("1 არ არის მარტივი რიცხვი. სცადეთ სხვა რიცხვი.")
#         mcdeloba += 1
#         continue

#     for i in range(2, num):
#         if num % i == 0:
#             print('Your number is not a prime')
#             count += 1
#             break
    
#     if count == 0:
#         print('your number is a prime')
#         break

#     mcdeloba += 1

# if mcdeloba == 3:
#     print("3 არასწორი მცდელობა იყო მეტი შანსი არ გაქვთ :)!")










# 4)ეს შედარებით რთულია და თუ ვერ გააკეთეთ არაუშავრა
# მომხმარებელს შემოატანინეთ რაიმე stringი და for ციკლის გამოყენებით დააბრუნეთ ეს სტრინგი შემოტრიალებული


# user_string = input("Enter string: ")
# string_reverse = ""

# for i in user_string:
#     string_reverse = i + string_reverse

# print(string_reverse)


# 2 გზა 

# print(user_string[::-1])