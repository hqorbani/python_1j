#create function تابع
def area_triangle(width , height):
    area = round(height * width / 2 , 2)
    print(f"area for width {width} and height {height} is: " , area)

def area_circle(r):
    print("circle area is" , r *r * 3.14)
    