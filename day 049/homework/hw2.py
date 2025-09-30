

# 2. შექმენი ორი set, იპოვე და დაბეჭდე მათში საერთო ელემენტები.


set1 = {"hi", "hello", "privet"}
set2 = {"hi", 3, 5}

for i in set1:
    if i in set2:
        print(i)