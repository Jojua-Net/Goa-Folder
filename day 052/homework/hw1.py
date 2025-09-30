

# 1) ლუწი და კენტი
# დაწერე პროგრამა, რომელიც მომხმარებლისგან 
# მიიღებს რიცხვს და დაბეჭდავს არის თუ არა ის ლუწი თუ კენტი.



def odd_or_even(num):
    if num % 2 == 0:
        return "ლუწია"
    else:
        return "კენტია"
    


print(odd_or_even(10))
print(odd_or_even(5))