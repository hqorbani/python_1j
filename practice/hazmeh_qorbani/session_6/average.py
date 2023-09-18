#### دستورالعمل ها
# اگر لیستی از اعداد داشته باشیم
# میخواهیم میانگین اعداد بخشپذیر بر عدد 3 را بدست آوریم
# عددی بر ۳ بخشپذیر است که باقیمانده تقسیم آن بر ۳ صفر باشد
# میانگین اعداد برابر است با حاصل جمع اعداد تقسیم بر تعداد اعداد
# code has been copied from Fatemeh Rouhafzaee:
numbers = [154,322,21,64,233,125,24]
number = []
for item in numbers :
    if item % 3 == 0 :
      number.append(item)
if len(number) > 0:
   print(sum(number) / len(number))
else:
   print("I did not find any number for result")



