

# user_num = int(input("Enter Number: "))
# result = 1
# for i in range(1, user_num+1):
#     result = result * i 
#     print(i, result)


# s = input("Input pleas: ") # Reverse 
# res = ''
# for i in s:
#     res = i + res
#     print(res)




# მომხარებელს შემოატანინეთ რაიმე რიცხვი, შემდეგ 
# for ციკლის გამოყენებით შეამოწმეთ, არის თუ არა ეს რიცხვი მარტივი, 
# თუ არის დაპრინტეთ "your number is a prime" თუ არ არის დაპრინტეთ "your number is not a prime"


# usernum = int(input("Enter number: "))
# count = 0

# while num == 1:
#     num = int(input('invalid input, try again: '))
# for i in range(2,usernum):
#     if usernum % i == 0 and count == 0:
#         print("your number is not a prime")
#         count += 1
# if count == 0:
#     print("your number is a prime")



print("the password has to be over 8 characters, must contain an upper character and must have a number")
password = input('please inpt a password: ')
while len(password) < 8 or 'A' not in password:
    password = input('please inpt a password: ')
print('Correct')












