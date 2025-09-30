


# 3)  დაწერე ფუნქცია is_even(number), რომელიც შემოწმებს რიცხვი ლუწია თუ კენტი.

# მომხმარებელმა შეიყვანოს 3 რიცხვი, გამოიძახე ფუნქცია და დაბეჭდე შედეგი:

# "Number <x> is even"

# "Number <x> is odd"




def is_even(number):
    if number % 2 == 0:
        return f"Number {number} is even"
    else:
        return f"Number {number} is odd"
    

print(is_even(9))
print(is_even(16))