# 5. მოცემულია set და ერთი მნიშვნელობა — შეამოწმე, შეიცავს 
# თუ არა set ეს მნიშვნელობა და დაბეჭდე შესაბამისი შეტყობინება.


def includes(arry, item):
    if item in arry:
        return f"ეს '{item}' არის set-ში"
    return f"ეს '{item}' არ არის set-ში"


print(includes({10, 20, "vaxo"}, "vaxo"))
print(includes({10, 20, "vaxo"}, 5))