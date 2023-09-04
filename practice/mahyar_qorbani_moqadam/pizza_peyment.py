pizza_name = input("please select a pizza name: ").lower()
if pizza_name == 'peperoni' or pizza_name == 'mix':
    pizza_number = int(input("please select pizza number: "))
    if pizza_number > 0:
        if pizza_name == "peperoni":
            pizza_price = 5
        elif pizza_name == "mix":
            pizza_price = 4

        payment = pizza_price * pizza_number

        print("your pizza name: ", pizza_name)
        print("your pizza number: ", pizza_number)
        print("payment price : ", payment , "$")
    else:
        print("please check your pizza number. it must be greater than 0.")
else:
    print("please check your pizza name. it was False.")