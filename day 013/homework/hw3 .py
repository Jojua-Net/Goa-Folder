# დაწერეთ პროგრამა რომელიც კლავიატურიდან შეტანილ მთელი რიცხვს გაზრდის
# 5-ით, თუ ის ლუწია და გაზრდის 3-ჯერ, თუ კენტია, შემდეგ კი შეინახავს მათი
# ჯამის 5-ზე გაყოფის ნაშთს და დაბეჭდავს ეკრანზე.


user_num = "123456789"
user_nums = 0
for i in user_num:
    if int(i) % 2 == 0:
        user_nums = user_nums + int(i) + 5
    elif int(i) % 2 != 0:
        user_nums = user_nums + int(i) + 3

print(user_nums % 5)