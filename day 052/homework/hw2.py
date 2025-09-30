


# 2) რიცხვების ჯამი
# მომხმარებელს შემოატანინე 5 რიცხვი
#  და იპოვე მათი ჯამი და საშუალო.



numbers = [   int(input("enter num 1: ")), int(input("enter num 2: ")), int(input("enter num 3: ")), int(input("enter num 4: ")), int(input("enter num 5: "))   ]

total = sum(numbers)

sashvalo = total / len(numbers)

print(total)
print(sashvalo)