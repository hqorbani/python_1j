print("wellcome to the pizza menu")
print("margarita = 5")
print("mix = 12")
name_pizza =input("enter your favorite pizza name")
number = int(input("enter your pizza number"))
if name_pizza == "mix":
    gheymat = 12
elif name_pizza == "makhsos":
    gheymat = 5
else:
    gheymat = 0
    print("we don't have this pizza in menu")
mablagh = number * gheymat
print("pizza name :" , name_pizza)
print("pizza number :" , number)
print("price :" , mablagh)