####  بازی حدس عدد

### دستور کار
#### برنامه ای بنویسید که عددی تصادفی بین ۱ تا ۱۰۰ تولید کند و از کاربر بخواهد که آن را حدس بزند.
#### کاربر ۱۰ مرتبه اجازه حدس زدن را دارد
#### اگر در مرتبه اول درست حدس بزند با ۱۰۰ امتیاز برنده بازی معرفی خواهد شد.
#### در غیر این صورت به ازای هر مرحله اشتباه حدس زدن ۱۰ امتیاز از ۱۰۰ کسر خواهد شد.

#### برنامه باید متناسب با حدس کاربر او را راهنمایی کند. 
#### برای نمونه اگر عدد تصادفی تولید شده ۲۶ می باشد و دراولین مرتبه کاربر ۷۲ را حدس می زند راهنمایی برنامه می تواند این باشد که جواب کمتر از حدس شماس و عددی کمتر از ۷۲ را حدس بزنید. همینطور برای مقدار پایین تر از جواب راهنمایی کند که باید عدد بیشتری را حد بزنید.
#### اگر کاربر در مرحله هفتم به جواب رسید بخاطر کم شدن هفت ۱۰ امیتاز با امتیاز ۳۰ برنده اعلام خواهد شد.
#### اگر کاربر در هیچ مرحله ای موفق به حدس جواب نشود بازنده معرفی خواهد شد و پیشنهاد دوباره شرکت در بازی اعلام خواهد شد.


#### چنانچه بخواهید قبل از تعداد دفعات تکراری که در حلقه تعیین کرده اید از حلقه خارج شود میتوانید از دستور break استفاده کنید


# geuss number game:
import random as r
r_number = r.randint(1,100)
# print(r_number)
print("")
print("*********--------*********-------")
print("You have played the number guessing game.")
print()
print("A number is chosen by the computer and you can guess this number 10 times.")
print("If you guess the first time, you will win with the most points, i.e. 100 points, and")
print("if you guess correctly the last time, you will win with 10 points.")
print("Otherwise, you will be out of the game as a loser.")
print("*********--------*********-------")
win = 0
counter = 100
while counter > 0:
    user_input=int(input("enter your guess: "))
    if (user_input == r_number):
        win = 1
        break
    elif user_input > r_number :
        print ("your geuss is GREATER than the answer, please try again...")
    elif user_input < r_number :
        print ("your geuss is LESS than the answer, please try again...")
    counter -= 10
if win == 1:
    print ('*-*-*-*-**-*-*-*-**-*-*-*-**-*-*-*-*-*-*-*-*-*-*')
    print ('*-*-*-*-*   YOU WON , congratulation   *-*-*-*-*')
    print (f'*-*-*-*-*  Your score is {counter} out of 100 *-*-*-*-*')
    print ('*-*-*-*-**-*-*-*-**-*-*-*-**-*-*-*-*-*-*-*-*-*-*')
else:
    print("you lose")
