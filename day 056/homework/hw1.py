
#!!!!! ეს დასასრულებელი მაქვს !!!!!!#

# 1) დაწერე ფუნქცია, რომელიც იღებს 
# სტრინგს და აბრუნებს ყველაზე ხშირ სიმბოლოს მასში.
# მაგალითი: "banana" → "a"

def frequent_char(word):

    chars = []

    
    
    
    for i in range(len(word)):
        if f"{word[i]} {word.count(word[i])}" not in chars:
            chars.append(f"{word[i]} {word.count(word[i])}")
        else:
            continue



    print(chars)




    new_chars = []

    for i in chars:
        i = i.split(" ")
        for x in i:
            new_chars.append(x)

    print(new_chars)

frequent_char("vaxoo")


