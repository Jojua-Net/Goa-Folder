# 4) მომხმარებელს შემოატანინეთ ნებისმიერი სიტყვა, შემდეგ ამ სიტყვიდან 
# გამოიტანეთ მხოლოდ 'A' ასოები, თუ არ შეიცავს 'A'ს გამოიტანეთ ცარიელი სტრინგი


user_word = input("Enter word: ")

for word in user_word:
    if word != "A":
        print(" ")
    elif word == "A":
        print(word)
    else:
        pass