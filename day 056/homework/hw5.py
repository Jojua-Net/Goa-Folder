



# 5) დაწერე ფუნქცია, რომელიც იღებს სტრინგს და აბრუნებს True თუ მასში ყველა ასო უნიკალურია, False — თუ რომელიმე მეორდება.
# მაგალითი: "python" → True, "hello" → False


def z(text):
    my_list = []

    for i in range(len(text)):
        if text.count(text[i]) == 1:
            my_list.append("კი")
        else:
            my_list.append("არა")


    for i in my_list:
        return my_list.count(i) == len(my_list)


print(z("vaxo"))
print(z("mari"))
print(z("gio"))
print(z("rogor xar?"))
print(z("xaxvii"))