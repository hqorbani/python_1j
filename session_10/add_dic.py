pizzas = {
    "peperoni":15,
    "meat":12,
    "margarita":7
    }
print(pizzas)
new_pizza_name = input("please enter new pizza name:")
new_pizza_price = float(input("please enter new pizza price:"))
pizzas[new_pizza_name] = new_pizza_price
print(pizzas)