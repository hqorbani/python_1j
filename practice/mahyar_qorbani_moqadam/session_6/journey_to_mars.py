names = []
countor = 1
while countor <= 3:
    brith_year = int(input("plase enter brith year")) 
    age =1402-brith_year
    if 20 < age < 28 :
        countor+=1
        name =input("pleas enter new name :")
        names.append (name)
        # print(names)
        for item in names:
            print(item)
    else :
        print("you can not enter")