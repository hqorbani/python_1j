while agree =='yes':
    a =int(input("enter the number greater than zero:"))
    b =int(input("enter the number greater than zero:"))
    c =int(input("enter the number greater than zero:"))
    if a + b >= c and b + c >= a and a + c >= b:
        if a == b and b == c:
            print("your triangle is equilateral")
        elif a == b and b != c:
            print("your triangle is motasavi saqeyn")
        elif c != b and a != c:
            print("your triangle is meghyasi")
        else:
            print("that is a scale")
    else:
        print("adade vared shode emkan tashkil mosalas nadarand.")
    agree = input("would you like try again?(yes/no) ") 
print("finished")