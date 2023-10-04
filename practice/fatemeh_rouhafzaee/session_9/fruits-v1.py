fruits = {
    "apple" : 6 ,
    "orange" : 5.5 ,
    "banana" : 11 ,
    "grapes" : 6 ,
    "coconat" : 14 ,
    "lemon" : 4.5 ,
    "melone" : 10 ,
    "kiwi" : 4.5 ,
    "cherry" : 6 ,
    "papaya" : 11,
    "pineapple" : 14 ,
    "watermelon" : 7 ,
    "avacado" : 13 ,
}
sum_of_price = sum(fruits.values())
max_price = max(fruits.values())
min_price = min(fruits.values())
max_price_fruits = []
min_price_fruits = []
min_10_price_fruits = []
max_10_price_fruits = []
average_price_fruits = []
for fruit_name , fruit_price in fruits.items():
    if fruit_price == max_price:
        max_price_fruits.append(fruit_name)
    elif fruit_price == min_price:
        min_price_fruits.append(fruit_name)
    elif fruit_price < 10 : 
        min_10_price_fruits.append(fruit_price)
    elif fruit_price > 10 :
        max_10_price_fruits.append(fruit_price)
    average_price_fruits.append(fruit_price)
print("max price:", max_price)
print(max_price_fruits)
print()
print("min price:", min_price)
print(min_price_fruits)
print()
print("sum of fruits price:",sum_of_price)
print()
print("min_10_price_fruits:" , sum(min_10_price_fruits))
print()
print("average_price_fruits:" , sum(average_price_fruits)/len(average_price_fruits))
print()
print("average_max_10_price_fruits:" , sum(max_10_price_fruits)/len(max_10_price_fruits))




