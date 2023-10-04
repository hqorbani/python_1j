agrea = "yes"
while agrea == "yes":
    print("salam khosh amadid")
    print("dar sorat vared nakardan moshakhasat asli dar mavaghe broz hadese be groh tahie konande marbot nemi bashad")
    name=input("name khod ra vared konid: ")
    last_name=input("famil khod ra vared konid: ")
    print("khosh amadid" , name , last_name)
    birth_year = int(input("sale tavalod khod ra benevis: "))
    age = 1402 - birth_year
    print("your age is " + str(age))
    if 13 <= age <= 19:
        print("you are teenager")
    else:
        print("you aren't teenager")
    print("khosh amadid be frosh gahe hamegani")

    print("ham zan = 12$")
    print("khord kon = 50$")
    print("zrofe chini = 94$")
    print("cheeps = 20$")
    print("pofack = 24$")
    print("mavade shoyande = 35$")
    print("shish lik = 100$")
    print("ja klidi = 13$")
    print("soda = 10$")
    print("shirini = 112$")

    name_kala =input("name kala ra vared konid:")
    number = int(input("tedad kala ra vared konod"))
    if name_kala == "ham zan":
        gheymat = 12
    elif name_kala == "khord kon":
        gheymat = 50
    elif name_kala == "zrofe chini":
        gheymat = 94
    elif name_kala == "cheeps":
        gheymat = 20
    elif name_kala == "pofack":
        gheymat = 24
    elif name_kala == "mavade shoyande":
        gheymat = 35 
    elif name_kala == "shish lik":
        gheymat = 100
    elif name_kala == "ja kilidi":
        gheymat = 13
    elif name_kala == "soda":
        gheymat = 10
    elif name_kala == "shirini":
        gheymat = 112
    elif name_kala == "zrof chini":
        print("in kala 30% takhfif darad")
    elif name_kala == "cheeps":
        print("in kala 10% takhfif darad")
    elif name_kala == "shirini":
        print("in kala 50% takhfif darad")
    else:
        gheymat = 0
        print("ma in kala ra nadarim")
        agrea = "no"
        agrea = input("mikhay dobare emtehan koni yes/no:")
    mablagh = number * gheymat
    print("name kala :" , name_kala)
    print("tedad kala :" , number)
    print("gheymat :" , mablagh)