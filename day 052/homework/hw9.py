


# 9) გამრავლების ტაბულა
# მომხმარებლის მიერ შეყვანილი რიცხვისთვის
#  დაბეჭდე მისი გამრავლების ტაბულა (1–დან 10-მდე).




def tabula(user_num):
        
    for i in range(11):
        print(f"{user_num} * {i} = {user_num * i}")
        
    return "მორჩა"


tabula(1)
tabula(5)
tabula(10)