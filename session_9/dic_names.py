pizzas ={
    "peperoni": 6,
    "mix": 5,
    "margarita":4
}

agree = "yes"
print("welcome ,  ")
while agree == 'yes':
    print("please select your order:")
    for pizza_name , pizza_price in pizzas.items():
        print(pizza_name , pizza_price , "$")
    seleted_pizza = input(" which one do you want? ")
    if seleted_pizza in pizzas:
        print("your select is" , seleted_pizza)
        agree = "no"
    else:
        print("please choose again. it's wrong...")
        agree = input("would you like see menu again?(yes/no)")
