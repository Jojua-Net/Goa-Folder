# 1. "გადათარგმნეთ" ფსევდო კოდი Python-ზე.

user = {
    "login": "Vaxo",
    "password": "12345678"
}

start = True
while start == True:
    login = input("enter login: ")
    password = input("enter password: ")

    if login != user["login"] and password != user["password"]:
        print("თქვენი ავტორიზაციის ინფორმაცია არასწორია სცადეთ ახლიდან!")
    else:
        if login == user["login"] and password == user["password"]:
            print("თქვენ ავტორიზაცია წარმატებით გაიარეთ!")
            break