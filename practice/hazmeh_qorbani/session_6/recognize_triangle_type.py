## تشخیص نوع مثلث
#### اطلاعات سه ضلع از یک مثلث را دریافت کنید مشخص کنید که مثلث متساوی الاضلاع، متساوی الساقین یا مقیاسی است.
### .
### در یک مثلت متساوی الاضلاع طول هر سه ضلع با هم برابر هستند
### .
### یک مثلث متساوی الساقین حداقل دو ضلع با طول یکسان دارد. (گاهی مشخص می شود که دقیقاً دو ضلع یکسان دارند، اما برای اهداف این تمرین حداقل دو ضلع را می گوییم.)
### .
### یک مثلث مقیاسی تمام اضلاع با طول های مختلف دارد.
### .
### توجه داشته باشید برای اینکه یک شکل اصلاً مثلثی باشد، طول تک تک ضلع ها باید بزرگتر از صفر باشد و مجموع طول های هر دو ضلع باید بزرگتر یا مساوی طول ضلع سوم باشد.
### .
### در معادلات: اگر a, b, c سه ضلع یک مثلث باشند پس باید موارد زیر در مورد آنها صادق باشند:
## a + b ≥ c
## b + c ≥ a
## a + c ≥ b

while agree =='yes':
    a =int(input("enter the number greater than zero:"))
    b =int(input("enter the number greater than zero:"))
    c =int(input("enter the number greater than zero:"))
    if a + b >= c and b + c >= a and a + c >= b:
        if a == b and b == c:
            print("your triangle is equilateral")
        elif a == b and b != c:
            print("your triangle is motasavi saqeyn")
        elif c != b and a != c:
            print("your triangle is meghyasi")
        else:
            print("that is a scale")
    else:
        print("adade vared shode emkan tashkil mosalas nadarand.")
    agree = input("would you like try again?(yes/no) ") 
print("finished")