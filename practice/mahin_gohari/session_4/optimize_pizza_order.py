print("wellcome pizza menu")
print("meat = 8")
print("peperoni = 9")
pizza_name =input("please enter your favorite pizza name: ")
if pizza_name == "meat" or pizza_name == "peperoni":
    pizza_namber =int(input("please enter your pizza namber: "))
    if pizza_name == "Meat" or pizza_name == "meat":
        pizza_price = 8
    else:
        pizza_price = 9
    if pizza_price > 0:
        payment = pizza_namber * pizza_price
        print("your pizza name: ", pizza_name)
        print("your pizza namber: ", pizza_namber)
        print("payment price : ", payment , "$")
else:
    print("we don't have this pizza on the menu")