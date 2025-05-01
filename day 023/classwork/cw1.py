# 1. შემოატანინეთ მომხმარებელს თავისი ასაკი და შეამოწმეთ, 
# თუ ის 10-წლისაა ან უფრო პატარა, დაპრინტეთ "Kid", 
# თუ 10-ზე მეტი და 18-ზე ნაკლები გამოიტანეთ "teenager", თუ 18-ზე მეტია 
# და 30-ზე ნაკლები "adult", სხვა შემთხვევაში "unc"
user_age = int(input("Enter your age: "))

if user_age <= 10:
    print("Kid")
elif user_age > 10 and user_age <= 18:
    print("teenager")
elif user_age > 18 and user_age <= 30:
    print("adult")
else:
    print("unc")