## سفر به مریخ
#### در نظر بگیرید کشوری برای مهاجرت و زندگی ۳ انسان به مریخ از بین جوانان بین  ۲۰ تا ۲۸ سال ثبت نام می‌کند.
#### اطلاعاتی ک حین ثبت نام پرسیده می‌شود نام و سال تولد افراد است.
#### برنامه این بنویسید که پس از ثبت نام ۳ نفر با شرایط گفته شده ، نام آنها را نمایش دهد.
#### پیشنهاد می شود برای نگهداری نام ها از لیست استفاده کنید.
# code has been copied from Fatemeh Rouhafzaee:
names = []
ages = []
u = 1
this_year = int (input("Please enter this year's date:"))
while u < 4 :
    name = input ("please enter your name :")
    year = int (input("please enter your year_birth :"))
    age = this_year - year 
    if 19 < age < 29 :
        names.append(name)
        ages.append(age)
        u = u + 1
    else :
        print("You can not register..")
    i = 0 
while i < 3 :
    print(names[i] , "_" , ages[i] , ":" , "You are accepted in this plan.....")
    i = i + 1 