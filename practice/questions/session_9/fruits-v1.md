#### دستور کار

### اگه ی دیکشنری از اسامی میوه ها بهمراه قیمت آنها داشته باشیم. موارد زیر را محاسبه کنید:

### بیشترین قیمت چند است و مربوط به چه میوه هایی است؟
### کمترین قیمت چند است و مربوط به چه میوه هایی است؟
### جمع قیمت تمام میوه ها چقدر است؟
### چمع قیمت میوه های کمتر از 10 دلار چقدر است؟
### میانگین قیمت میوه ها چقدر است؟
### میانگین قیمت میوه های بالای 10 دلار چقدر است؟

```python

# tips and guide
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
    "avacado" : 13
}
# sum of dictionary values
print(sum(fruits.values()))

# max of dictionary values
print(max(fruits.values()))

# min of dictionary values
print(min(fruits.values()))
```
