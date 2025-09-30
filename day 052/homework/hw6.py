


# 6) პალინდრომი
# დაწერე პროგრამა, რომელიც ამოწმებს 
# სიტყვა არის თუ არა პალინდრომი (მაგ. ana, level).

def palindrome(text):

    if text == text[::-1]:
        return "პალინდრომია"
    else:
        return "არ არის პალინდრომი"
    

print(palindrome("level"))


