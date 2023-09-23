fruits = {
    "apple":5,
    "orange":6,
    "benana":4,
    "lemon":8,
    "melon":3
}
# for key , value in fruits.items():
#     print(key ,"==>", value)
# #-----------
# for key , value in fruits.items():
#      if value > 5:
#         print(key ,"==>", value)
#-----------
# for fruit in fruits:
#     # print key , value
#     print(fruit , fruits[fruit])
#----------
# for fruit in fruits.values():
#     print(fruit)
# print("sum of fruits prices: ",sum(fruits.values()))
#-----------------

for fruit_name , fruit_price in fruits.items():
    print(fruit_name ,"==>", fruit_price)