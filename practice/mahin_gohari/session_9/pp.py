print("welcome , pizza menu:")
pizza = {
    "peperoni":15,
    "meat":12,
    "margarita":7
    }
agree = "yes"
while agree == 'yes':
    print("please select your order:")
    for pizza_name , pizza_price in pizza.items():
        print(pizza_name , pizza_price , "$")
    seleted_pizza = input(" which one do you want? ")
    if seleted_pizza in pizza:
        print("your select is" , seleted_pizza)
        agree = "no"
    else:
        print("please choose again. it's wrong...")
        agree = input("would you like see menu again?(yes/no)")
    pizza_number = int(input("how many pizza do you want?"))
    if pizza_number > 0:
        if seleted_pizza == "peperoni":
            pizza_price = 15
        elif seleted_pizza == "meat":
            pizza_price = 10
        elif seleted_pizza == "margarita":
            pizza_price = 7

    payment = pizza_price * pizza_number

    print("your pizza name: ", seleted_pizza)
    print("your pizza number: ", pizza_number)
    print("payment price : ", payment , "$")
    