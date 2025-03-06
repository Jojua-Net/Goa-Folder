import random

# 5. შექმენით პატარა თამაში, სადაც თქვენ შექმნით რაიმე რიცხვების თანმიმდევრობას,
# და მომხმარებელმა კი უნდა გამოიცნოს ეს თანმიმდევრობა (გამოიყენეთ While loop)


saidumloricxvi = random.randint(1, 10)
user_number = int(input("შეიყვანე რიცხვი რომელსაც ფიქრობ (1-იდან 10-მდე): "))


while user_number != saidumloricxvi:
    user_number = int(input("შენი რიცხვი არასწორია, სცადე თავიდან: "))

    if user_number == saidumloricxvi:
        print(f"სწორია!! საიდუმლო რიცხვი არის {saidumloricxvi}")
