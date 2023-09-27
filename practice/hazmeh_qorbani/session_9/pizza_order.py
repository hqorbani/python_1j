print("welcome , pizza menu:")
pizzas = {
    "peperoni":15,
    "meat":12,
    "margarita":7
    }
chashni={
    "cheese":1,
    "pepper":2
}
off_codes={
    "paeez":2
}
agree = "yes"
while agree == 'yes':
    print("please select your order:")
    for pizza_name , pizza_price in pizzas.items():
        print(pizza_name , pizza_price , "$")
    seleted_pizza = input(" which one do you want? ")
    if seleted_pizza in pizzas:
        print("your select is" , seleted_pizza)
        agree = "no"
        pizza_number = int(input("how many pizza do you want?"))
        if pizza_number > 0:
            # pizzas[seleted_pizza] means selected pizza price
            payment = pizzas[seleted_pizza] * pizza_number

            print("your pizza name: ", seleted_pizza)
            print("your pizza number: ", pizza_number)
            print("payment price : ", payment , "$")
        else:
            print("please choose again. it's wrong in number of pizza...")
            agree = input("would you like see menu again?(yes/no)")
 
                            
    else:
        print("please choose again. it's wrong...")
        agree = input("would you like see menu again?(yes/no)")


