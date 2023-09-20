name = input("enter your name:")
birth_year = int(input("enter you birth year:"))
age= 1402 - birth_year
if 15 < age < 23:
    print("your teenager")
Weight = int(input("enter your weight (kg):"))
if Weight <= 18.5:
    print("you have Underweight.")
elif Weight >= 18.5 <= 24.9:
    print("your normal.")
elif Weight >= 25 <= 29.9:
    print("you have Overweight.")
elif Weight >= 30 <= 34.9:
    print("you have Excessive weight gain.")
elif Weight <= 35:
    print("you have excessive obesity.")
height = int(input("Enter your height (m) :"))
bmi = print("bmi :" , Weight / height ** 2)
print("finish")