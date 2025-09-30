


# 4) dictionary students:

# students = {
#     "Ana": 95,
#     "Giorgi": 88,
#     "Luka": 76
# }


# Loop-ით დაბეჭდე მხოლოდ ის სტუდენტები, ვინც ქულა >= 90-ია.

# დაამატე ახალი სტუდენტი "Nino": 100 update()-ით.

# დაბეჭდე dictionary საბოლოო სახით.


students = {
    "Ana": 95,
    "Giorgi": 88,
    "Luka": 76
}


for i in students.keys():
    if students[i] >= 90:
        print(i)

students.update({"Nino": 100})

print(students)
