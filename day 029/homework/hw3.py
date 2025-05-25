# 3. გამოიყენეთ Comprasion Operations და 
# Logical Operations ერთად, შეეცადეთ 
# კომენტარებით ახსნათ რატომ გამოაქვს 
# ესეთი შედეგი და ასევე თუ რომელი 
# სრულდება პირველი, რა თანმიმდევრობით.


# Comprasion Operations & Logical Operations


    #  TRUE  AND  FALSE OR  TRUE
print(10 > 5 and 5 > 15 or 30 > 10) # OUTPUT: True 

# მოკლედ აქ გამოვიყენე ორივე ოპერატორი ერთად რადგან 10 > 5-ზე ეს აბრუნებს Logical Operations
# ანუ True ან False-ს გვიბრუნებს ჩვენ Comprasion Operations ხოდა მოკლედ ეხლა
# რომ მივყვეთ ჩვენ 10 > 5 ეს დააბრუნებს True-ს შემდგომ 5 > 15-ზე ეს დააბრუნებს False-ს რადგან
# 5 არ არის მეტი 15-ზე ხოდა მაგიტომ აბრუნებს False შემდგომ უკვე შესრულდება 30 > 10-ზე ეს აბრუნებს True-ს
# და ეხლა საბოლოოდ Logical Operations-ს რომ მივყვეთ პირველი სრულდება and operator-ი შემდგომ or operator-ი
# პირველი შესრულდება 10 > 5 = True and 5 > 15 = False |= False რადგან and operator-ში ერთერთი მაინც თუ მცდარია მაშინ აბრუნებს False-ს ხოლო
# შემდგომ უკვე სრულდება or operator-ი და მის შემთხვევაში 10 > 5 = True and 5 > 15 = False |= (False or True) თუ ერთერთი მაინც არის სწორი ანუ მცადარი "ან" მართალი მაშინ ის დააბრუნებს მართალს ანუ True

