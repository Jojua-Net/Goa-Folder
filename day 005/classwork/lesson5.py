

# name = "Group65GGG"
# res = "zd"
# for i in name:
#     if i == 'G':
#         res = res + i
# print(res)





# 1) for ციკლით გადაუარეთ რიცხვებს 2-დან 25-მდე და გამოიტანეთ მხოლოდ კენტი რიცხვები

# 1) დავალება

# for i in range(2, 25):
#     if i % 2 == 1:
#         print(i)


# 2) მომხმარებელს შემოატანინეთ სახელი inputის დახმარებით, შემდეგ for ციკლით გადაუარეთ ამ სახელს და გამოიტანეთ თვითოეული ასო ცალ-ცალკე

# 2) დავალება

# user_name = str(input("Enter name: "))

# for i in user_name:
#     print(i)






# seats = 10
# while seats > 0:
#     print("Seat sold")
#     seats = seats - 1

# age = 10
# while age < 18:
#     print("you are a kid")
#     age += 1




# 3) შექმენით correct_password ცვლადი სადაც შეინახავთ რაიმე პაროლს, შემდეგ მომხმარებელს inputით შემოატანინეთ რაიმე პაროლი, სანამ ეს მომხმარებლის შემოტანილი პაროლი არ უდრის correct_passwordს თავიდან შემოატანინეთ მომხმარებელს პაროლი

# 3) დავალება
user_password = input("Enter password: ")
correct_password = "vaxtang1234"

while user_password != correct_password:
    user_password = input("Enter password: ")

