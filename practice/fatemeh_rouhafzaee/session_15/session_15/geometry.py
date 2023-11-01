def check_traingle(side_1 , side_2 , side_3 ) -> bool:
    if side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_2 + side_3 > side_1:
        return True
    else:
        return False
    
def area_triangle(width , height):
    return round(height * width / 2 , 2)
    
def environment_triangle(side_1 , side_2 , side_3 ) :
        return round(side_1 + side_2 + side_3 , 2)
    
def area_circle(r):
    return round( r *r * 3.14 , 2)

def environment_circle(r) :
    return round((r*2)*3.14 , 2)

def area_square (Square_side) :
    return round(Square_side * Square_side , 2)

def environmen_square(Square_side) :
    return round(Square_side * 4 , 2)

def area_rectangle(width , length) :
   return round(width * length , 2)

def environmen_rectangle(width , length) :
   return round((width + length) * 2) 

def erea_trapezius(big_side , small_side , Height ) :
    return round(((big_side + small_side) *Height) / 2 , 2) 

def environmen_trapezius(c_side , d_side ,big_side , small_side ) :
    return round(c_side + d_side + big_side + small_side , 2 )  

def area_rhombus(a_Diameter , b_Diameter) :
    return round((a_Diameter * b_Diameter) / 2 , 2)

def environmen_rhombus(a_side , b_side , c_side , d_side) :
    return round(a_side + b_side + c_side + d_side , 2)