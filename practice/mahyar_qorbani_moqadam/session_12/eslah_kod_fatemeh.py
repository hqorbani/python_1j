import random as r
selected_number = r.randint(1 , 35)
o = 1
win = 0
emtiaz =100
while o < 11 :
    answer =int (input("Please enter your desired number(1 , 35): "))
    if selected_number < answer :
        print("is bigger , try again...")
    elif selected_number > answer :
        print("is smaller,  try again...")
    elif selected_number == answer :
        win = 1
        break
    o = o + 1
    emtiaz -= 10
if win == 1:
    print("you win , congratulation")
    print("your emtiaz is" , emtiaz)
else:
    print ("You lose ")