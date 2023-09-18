#### دستورالعمل ها
# اگر لیستی از اعداد داشته باشیم
#### برنامه ای بنویسید که بتواند موارد زیر را اعلام کند:
#### number_greater_than_100: تعداد اعدادی که مقدار آنها بزرگتر مسادی 100 است
#### number_smaller_than_100: تعداد اعدادی که مقدار آنها کمتر از 100 است
#### average_greater_than_100:  میانگین اعدادی که مقدار انها بزرگتر مساوی 100 است 
#### average_smaller_than_100:  میانگین اعدادی که مقدار انها کمتر از 100 است 
# code has been copied from Fatemeh Rouhafzaee:
numbers = [154,321,12,23,35,63,230,251,21,238,659,250,522,2541,12,10,19,18]
number_greater_than_100 = []
number_smaller_than_100 = []
for items in numbers :
    if items >= 100 :
     number_greater_than_100.append(items)
    elif items < 100 :
     number_smaller_than_100.append(items)    
print("number_greater_than_100: " , len(number_greater_than_100))
print("number_smaller_than_100: " , len(number_smaller_than_100))   
print("average_greater_than_100: " , round(sum(number_greater_than_100)/len(number_greater_than_100), 2))
print("average_smaller_than_100: " , round(sum(number_smaller_than_100)/len(number_smaller_than_100) , 2))


