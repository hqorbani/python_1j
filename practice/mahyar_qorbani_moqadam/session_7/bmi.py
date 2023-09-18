weight =int(input("please enter your weight in kg :"))
height =int(input("please enter your height in m :"))
bmi =weight / height ** 2
if bmi < 18.5:
    print("you are under weight :( ")
elif 18.5 <= bmi <= 24.9:
    print("you are normal weight :) ")
elif 25 <= bmi <= 29.9:
    print("you are over weight :] ")
elif 30 <= bmi <= 34.9:
    print("you are very over weight :[ ")
else:
    print("you are very very fat :( ")