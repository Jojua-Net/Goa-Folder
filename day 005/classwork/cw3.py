# 3) შექმენით correct_password ცვლადი სადაც შეინახავთ რაიმე პაროლს, შემდეგ მომხმარებელს inputით შემოატანინეთ რაიმე პაროლი, სანამ ეს მომხმარებლის შემოტანილი პაროლი არ უდრის correct_passwordს თავიდან შემოატანინეთ მომხმარებელს პაროლი

# 3) დავალება
user_password = input("Enter password: ")
correct_password = "vaxtang1234"

while user_password != correct_password:
    user_password = input("Enter password: ")
