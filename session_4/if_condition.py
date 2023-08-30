birth_year = int(input("please enter your birth year: "))
age = 1402 - birth_year
print("age: " , age)
if 13 <= age <= 19:
    print("you're a teenager")
    print("it's finished")
elif 20 <= age <= 26:
    print("you're a young person")
elif 27 <= age:
    print("you're a old person")
else:
    print("you're a child")
print("tamam shod.")