# برنامه ای بنویسید که کاربر اجازه انتخاب یک مدل پیتزا را داشته باشد
# و به تعداد بتواند سفارش دهد
#در انتها قیمت قابل پرداخت را محاسبه کنید و در خروجی نمایش دهید
# برای نمونه اگر قیمت پیتزا پپرونی 5 دلار باشد و کاربر 3 پیتزا پپرونی سفارش دهد باید قیمت پرداختی 15 دلار باشد
# peperoni : 5
# mix : 4
# نکته : شرط بررسی تساوی استفاده از 
# == 
# است
print("welcome , pizza menu:")
print()
print("peperoni : 5")
print("mix : 4")
print()  
pizza_name = input("please select a pizza name: ")
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
