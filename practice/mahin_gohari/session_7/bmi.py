name = input("what is your name?")
birth_year = int(input("what is your birth year?"))
age = 1402 - birth_year
if 13 < age < 19:
    print("your teenager.")
elif 13 >= age:
    print("your a child.")
elif 19 <= age:
    print("your a old person.")
weight = int(input("please enter your wight:"))
if weight <= 18.5: 
    print("you have underweight.")
elif weight >= 18.5 <= 24.9:
    print("you are normal.")
elif weight >= 25 <= 29.9:
    print("you have overweight.")
elif weight >= 30 <= 34.9:
    print("you have excessive weight gain.")
elif weight <= 35:
    print("you have excessive obesity.")
    print("finished.")
