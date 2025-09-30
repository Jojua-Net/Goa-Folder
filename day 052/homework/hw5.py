


# 5) ყველაზე დიდი რიცხვი
# მოცემული სიისგან (მაგ. [4, 7, 1, 9, 2]) 
# იპოვე ყველაზე დიდი რიცხვი max() ფუნქციის გარეშე.


numbers = [4, 7, 1, 9, 2]

max_number = numbers[0]


for i in numbers:
    if i > max_number:
        max_number = i

print(max_number)