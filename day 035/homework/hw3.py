# 3. დაწერეთ ამ ლოგიკით კოდი Python-ში:

age = int(input("Enter your age: "))

if age > 0 and age < 18:
    print("შენ არ ხარ სრულწლოვანი")
elif age < 0:
    print("დაბადებულიც არ ხარ ეს არასწორი პასუხია :დ")
else:
    print("შენ სრულწლოვანი ხარ")