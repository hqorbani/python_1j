print("welcome to the pizza resturant , pizza menu:")
pizzas = {
    "mix":15,
    "mushrooms and meat":12,
    "margarita":10
    }
chashni={
    "cheese":7,
    "onion":5,
    "nothing":0
}
drinks={
    "soda":9,
    "pepsi":6,
    "water":4,
    "nothing":0
}
off_codes={
"festival":10 , 
"paeez" : 2
}
user_off_percent = 0
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
            for chashni_name , chashni_price in chashni.items():
                print(chashni_name , chashni_price)
            seleted_chashni = input(" which one do you want? ")
            if seleted_chashni in chashni:
                print("your select is" , seleted_chashni)  
            for drink_name , drink_price in drinks.items():
                print(drink_name , drink_price)
            seleted_drinks =input("which one do you want?")
            if seleted_drinks in drinks:
                print("your select is" , seleted_drinks)
                user_off_code =input("enter off codes")
                if user_off_code in off_codes:
                    for off_code , off_percent in off_codes.items():
                        if off_code == user_off_code:
                            user_off_percent = off_percent

                    # code to calculate off code

                pizza_price = pizzas[seleted_pizza] + chashni[seleted_chashni] + drinks[seleted_drinks]
                payment = pizza_price * pizza_number
                payment_price = payment - (user_off_percent * payment / 100)
                print("your pizza name: ", seleted_pizza)
                print("your drink name:", seleted_drinks)
                print("your pizza number: ", pizza_number)
                print("payment price : ", payment_price , "$")

            else:
                print("please choose again. it's wrong in chashni type...")
                agree = input("would you like see menu again?(yes/no)")
        else:
            print("please choose again. it's wrong in number of pizza...")
            agree = input("would you like see menu again?(yes/no)")
 
                            
    else:
        print("please choose again. it's wrong...")
        agree = input("would you like see menu again?(yes/no)")

