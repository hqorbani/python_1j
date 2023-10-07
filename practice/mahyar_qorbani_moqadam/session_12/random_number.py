import random as r
r_number = r.randint(1,100)
win = 0
counter = 100
while counter > 0:
    user_input=int(input("enter your guess: "))
    if (user_input==r_number):
        win = 1
        break
    elif user_input > r_number :
        print ("your geuss is GREATER than the answer, please try again...")
    elif user_input < r_number :
        print ("your geuss is LESS than the answer, please try again...")
    counter -= 10
if win == 1:
    print ('*-*-*-*-**-*-*-*-**-*-*-*-**-*-*-*-*-*-*-*-*-*-*')
    print ('*-*-*-*-* congratulation , YOU WIN MY LOVE   *-*-*-*-*')
    print (f'*-*-*-*-*  Your score is {counter} out of 100 *-*-*-*-*')
    print ('*-*-*-*-**-*-*-*-**-*-*-*-**-*-*-*-*-*-*-*-*-*-*')
else:
    print("you lose :[ , you were bad at the game")
    print("I'M SO SORRY FOR YOU :(")