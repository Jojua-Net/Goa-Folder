
#!!!!! ეს დასასრულებელი მაქვს !!!!!!#

# 8) Guess the Number 🎲
# დააგენერირე შემთხვევითი რიცხვი 1–დან 100-მდე 
# და აცადე მომხმარებელს გამოიცნოს.
# ყოველი მცდელობისას მიუთითე: "მეტია" თუ "ნაკლებია".


import random

score = 0
guess_num = random.randint(1, 10)

print(guess_num)

user_num = int(input("enter your num: "))

while True:

    

    if user_num == guess_num:
        score += 5
        print(f"გილოცავ შენ გამოიცანი შენი ქულა არის {score}")
        

        user_answer = input("გინდა გარძელება (კი/არა)?: ")

        if user_answer == "კი":
            continue
        elif user_answer != "კი" or user_answer != "არა":
            print("თქვენი პასუხი არასწორია უნდა იყოს (კი/არა)!!!")
        else:
            break
        

    else:
        user_num = int(input("enter your num: "))
