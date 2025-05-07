# 2. შექმენით ფუნქცია, რომელიც მიიღებს მომხმარებლისგან არგუმენტს და მისი type-ის სესაბამისად გამოიტანეთ სიტყვები:
# Str - "Literature"
# Int/Float - "Math"
# Bool - "Science"

def type_check(x):
    if isinstance(x, str):
        return "Literature"
    elif isinstance(x, bool):
        return "Science"
    else:
        return "Math"
    

print(type_check("vaxo"))
print(type_check(5))
print(type_check(5.0))
print(type_check(True))