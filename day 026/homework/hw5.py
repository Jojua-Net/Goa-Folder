# 5. შექმენით ფუნქცია სადაც მომხარებელი შეიყვანს რაიმე 
# მათემატიკურ ოპერაციას 
# და თქვენ უნდა დააბრუნოთ საბოლოო პასუხის type.

def math_op(x, y, op):
    if op == "+":
        return type(x + y)
    elif op == "*":
        return type(x * y)
    else:
        if type(x) == int and type(y) == int:
            if op == "-":
                return type(x - y)
            elif op == "/":
                return type(x / y)
    
print(math_op(5, 10, "+"))
print(math_op(5, "10", "*"))
print(math_op(5, 10, "-"))
print(math_op(10, 5, "/"))