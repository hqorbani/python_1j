print("wellcome to the pizza menu")
print("makhlot = 8")
print("sosis = 1")
print("peperoni = 2")
name_pizza =input("name pizza ra vared konid:")
number = int(input("tedad pizza ra vared konid:"))
if name_pizza == "sosis":
    gheymat = 1
elif name_pizza == "makhlot":
    gheymat = 8
elif name_pizza == "peperoni":
    gheymat = 2
else:
    gheymat = 0
    print("we don't have this pizza in menu")
mablagh = number * gheymat
print("name pizza :" , name_pizza)
print("tedad pizza :" , number)
print("gheymat :" , mablagh)