
def area_triangle(width , height):
    area = round(height * width / 2 , 2)
    print(f"area for width {width} and height {height} is: " , area)
def check_traingle(side_1 , side_2 , side_3 ) -> bool:
    if side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_2 + side_3 > side_1:
        return True
    else:
        return False
def Environment_triangle(side_1 , side_2 , side_3 ) :
        return side_1 + side_2 + side_3
    
def area_circle(r):
    return round( r *r * 3.14)

def Environment_circle(r) :
    return round((r*2)*3.14)

def area_Square (Square_side) :
    print(f"area for Square_side{Square_side} is: " , round(Square_side * Square_side))

def Environmen_Square(Square_side) :
    print(f"Environmen_Square for Square_side{Square_side} is: " , round(Square_side * 4))

def area_Rectangle(width , length) :
    print(f"area for width{width} and length{length} is: " , round(width * length))

def Environmen_Rectangle(width , length) :
    print(f"Environmen_Rectangle for width{width} and length{length} is: " ,round((width + length) * 2)) 