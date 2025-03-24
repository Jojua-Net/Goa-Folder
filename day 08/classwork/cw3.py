# davaleba 3

user_string = input("Enter string: ")
while len(user_string)<3:
    user_string = input("თქვენ უნდა შეიყვანოთ ზუსტად 3 ასო: ")

    string_reverse = ""
    for i in user_string:
        string_reverse = i + string_reverse

    print(string_reverse)

    if user_string == string_reverse:
        print(True)
    else:
        print(False)