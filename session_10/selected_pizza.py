pizzas = {
    "peperoni":15,
    "meat":12,
    "margarita":7
    }
for pizza_name , pizza_price in pizzas.items():
    print(pizza_name , pizza_price , "$")
seleted_pizza = input(" which one do you want? ")
print(seleted_pizza , pizzas[seleted_pizza])
