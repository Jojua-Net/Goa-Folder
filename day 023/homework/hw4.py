
# 4. შექმენით ფუნქცია რომელიც დაუმატებს ერთმანეთს 
# string-ებს რომელიც გადმოეცემა არგუმენტად, 
# გაითვალისწინეთ რომ თუ რომელიმე არგუმენტი იქნება ineger 
# ის უნდა მოათავსოთ შედგენილი ქინადადების ბოლოშო.

def x(one, two):
    x = ""
    if isinstance(one, str):
        x += one
    elif isinstance(one, int):
        x += ""
    else:
        one = str(one)
    
    if isinstance(two, str):
        x += two
    elif isinstance(two, int):
        x += ""
    else:
        two = str(two)

    if isinstance(one, int):
        x += str(one)
    if isinstance(two, int):
        x += str(two)

    return x
    
print(x("Hello", "World"))
print(x("Age:", 25))
print(x(2025, "წელი"))
print(x(1, 2))
print(x("Test", True))
