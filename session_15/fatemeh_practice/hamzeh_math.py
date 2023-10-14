# from geometry import Environment_triangle , check_traingle
from geometry import *

side_1 = 15
side_2 = 30
side_3 = 15
if check_traingle(side_1 , side_2 , side_3) == True:
#or:
# if check_traingle(side_1 , side_2 , side_3):
    env_triangle = Environment_triangle(side_1 , side_2 , side_3)
    print("triangle env = " , env_triangle)
else:
    print("your sides are invalid.")