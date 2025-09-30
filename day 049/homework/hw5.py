

# 5. შექმენი რამდენიმე ობიექტი 
# (dictionary) და დაბეჭდე მხოლოდ ისინი, ვისი ასაკიც 18-ზე მეტია.


users_info = {
    "user1": {
        "name": "vaxo",
        "age": 16
    },

    "user2": {
        "name": "gio",
        "age": 18
    },

    "user3": {
        "name": "irakli",
        "age": 13
    },

}


for i in users_info.values():
    if i["age"] >= 18:
        print(i)