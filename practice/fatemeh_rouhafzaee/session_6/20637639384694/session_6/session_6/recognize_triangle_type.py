side_1 = int (input("Please enter the first side : "))
side_2 = int (input("Please enter the second side : "))
side_3 = int (input("Please enter the third side : "))
if side_1 + side_2 >= side_3 and  side_2 + side_3 >= side_1 and side_1 + side_3 >= side_2 :
    if side_1 == side_2 or side_2 == side_3 or side_1 == side_3 :
        print("This is a motasavi_saghain. ")
    elif side_1 == side_2 and side_2 == side_3 :
        print("This is a motasavi_azla.")     
    elif side_1 != side_2 and side_2 != side_3 :
        print("This is a meghiasi.")    
else :
    print("This is not a triangle...")        
