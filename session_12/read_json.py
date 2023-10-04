import json
json_data = open('pizzas.json')
pizzas_data = json.load(json_data)
json_data.close()
for pizza_name , pizza_price in pizzas_data.items():
    print("Pizza: ", pizza_name, "Price: $", pizza_price)
# print(pizzas_data)
# print(type(pizzas_data))