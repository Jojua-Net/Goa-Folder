


# 5) მომხმარებელმა შეიყვანოს 3 ქვეყნის სახელები.

# შექმენი dictionary, სადაც key = ქვეყანა, 
# value = დედაქალაქი (შენი არჩევანი).

# Loop-ით დაბეჭდე ქვეყანა + დედაქალაქი.

# მომხმარებელს ჰკითხე ქვეყანა და თუ არსებობს
#  dictionary-ში → დაბეჭდე დედაქალაქი, თუ არა → "Country not found"



qveynebi = {}


for i in range(3):
    qveyana = input(f"sheiyvane qveyana {i+1}: ")
    dedaqalaqi = input(f"sheiyvane dedaqalaqi {qveyana}: ")
    qveynebi[qveyana] = dedaqalaqi

print(qveynebi)

print("\nqveynebi da dedaqalaqebi:")
for qveyana, dedaqalaqi in qveynebi.items():
    print(f"{qveyana} -> {dedaqalaqi}")


kitxva = input("\nsheiyvane qveyana da ipove misi dedaqalaqi: ")

if kitxva in qveynebi:
    print(f"{kitxva}-s dedaqalaqia {dedaqalaqi} es")
else:
    print("Country not found")