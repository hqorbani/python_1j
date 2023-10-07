import json
json_data = open('pizzas.json')
pizzas_data = json.load(json_data)
# print(pizzas_data)

# Data to be written
new_pizza_name = input("please enter new pizza name: ")
new_pizza_price = float(input("please enter new pizza price: "))
pizzas_data[new_pizza_name] = new_pizza_price

 
# Serializing json
json_object = json.dumps(pizzas_data, indent = 4)
 
# Writing to pizzas.json
with open("pizzas.json", "w") as outfile:
    outfile.write(json_object)