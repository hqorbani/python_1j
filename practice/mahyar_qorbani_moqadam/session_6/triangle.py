a =int(input("enter the number greater than zero:"))
b =int(input("enter the number greater than zero:"))
c =int(input("enter the number greater than zero:"))
if a == b and b == c:
    print("your triangle is equilateral")
elif a == b and b != c:
    print("your triangle is isosceles")
elif c == b and a != c:
    print("your triangle is isosceles")
elif a == c and a != b:
    print("your triangle is isosceles")
else:
    print("that is a scale")