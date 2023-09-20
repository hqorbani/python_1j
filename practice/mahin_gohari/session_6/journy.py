names = []
counter = 1
while counter <= 3:
    counter += 1 
    birth_year = int(input("please enter your birth year:"))
    name = input("please enter new name:")
    names.append(name)
    age = 1402 - birth_year
    if 20 < age < 28:
        print("you can")
    else:
        print("you can't")
for item in names:
    print(item)