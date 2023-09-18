name = input("what is your name?")
birth_year = int(input("what is your birth year?"))
age = 1402 - birth_year
if 13 < age < 19:
    print("your teenager.")
elif 13 >= age:
    print("your a child.")
elif 19 <= age:
    print("your a old person.")
weight = int(input("how much do you weight? (kg)"))
height = int(input("what is your height? (cm)"))
height = height / 100
bmi = (weight / height ** 2)
if bmi <= 18.5:
    print("you have underweight.")
elif 18.5 <= bmi <= 24.9:
    print("you are normal.")
elif 25 <= bmi <= 29.9:
    print("you have overweight.")
elif 30 <= bmi <= 34.9:
    print("you have excessive weight gain.")
elif 35 <= bmi:
    print("you have excessive obesity.")
    print("finished.")
