# 3. მომხმარებელს შემოყავს პროექტში მიღებული ქულის შესახებ, თუ ის 90-ზე მეტია შეფასებაა A,
# თუ 75-ზე მეტია შეფასებაა B, თუ 60-ზე მეტია შეფასებაა C, თუ 50-ზე მეტია შეფასებაა D, თუ 40-ზე E და თუ 30-ზე F, Good Luck💚

user_score = int(input("Enter score: "))

if user_score >= 90:
    print("შეფასება: A")
elif user_score >= 75:
    print("შეფასება: B")
elif user_score >= 60:
    print("შეფასება: C")
elif user_score >= 50:
    print("შეფასება: D")
elif user_score >= 40:
    print("შეფასება: E")
elif user_score >= 30:
    print("შეფასება: F")