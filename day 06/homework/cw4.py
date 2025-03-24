
# 4)ეს შედარებით რთულია და თუ ვერ გააკეთეთ არაუშავრა
# მომხმარებელს შემოატანინეთ რაიმე stringი და for ციკლის გამოყენებით დააბრუნეთ ეს სტრინგი შემოტრიალებული


user_string = input("Enter string: ")
string_reverse = ""

for i in user_string:
    string_reverse = i + string_reverse

print(string_reverse)


# 2 გზა 

print(user_string[::-1])