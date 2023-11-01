from geometry import *


print("hi :))")
print("This program has the ability to calculate the area and perimeter of triangles, circles, rectangles , square ,rectangle , trapezius and rhombus  ")
print()
print("Please choose one of the options :")
print("1)triangle")
print("2)circle")
print("3)rectangle")
print("4)square")
print("5)trapezius")
print("6)rhombus")
print()
agree = "yes"
while agree == 'yes':
    Type_number =int (input("Please enter only the desired number :"))
    if 0 < Type_number < 7 : 
        if Type_number == 1 :
            width = float (input("Please enter the width :")) 
            height = float (input("Please enter the height :"))
            side_1 = float (input("Please enter side_1 :"))
            side_2 = float (input("Please enter side_2 :"))
            side_3 = float (input("Please enter side_3 :"))
            if check_traingle(side_1 , side_2 , side_3) == True:
                traingle_area = area_triangle(width , height)
                traingle_environment = environment_triangle(side_1 , side_2 , side_3 )
                print(f"area for width : {width} and height : {height} is: " , traingle_area )
                print(f"environment for side_1 : {side_1} , side_2 : {side_2} and side_3 : {side_3} is: " , traingle_environment )
                agree = str(input("would you like play again?(yes/no)"))
                if agree == "no" :
                    print("Thank you for using our app :)")    
            else:
                print("your sides are invalid.")
                agree = str(input("would you like play again?(yes/no)"))
                if agree == "no" :
                    print("Thank you for using our app :)")
        elif Type_number == 2 :
            r = float (input("Please enter the r :"))
            if r > 0 : 
                area_circle = area_circle(r)
                environment_circle = environment_circle(r) 
                print(f"area for r : {r} is: " ,  area_circle )
                print(f"environment for r : {r} is: " , environment_circle)
                agree = str(input("would you like play again?(yes/no)"))
                if agree == "no" :
                    print("Thank you for using our app :)")
            else :
                print("your r is invalid.")
            agree = str(input("would you like play again?(yes/no)"))
            if agree == "no" :
                    print("Thank you for using our app :)")
        elif Type_number ==3 :
            width = float(input("Please enter the width :"))
            length =float(input("Please enter the height :"))           
            if width and length > 0 :
                area_rectangle = area_rectangle(width , length)
                environmen_rectangle = environmen_rectangle(width , length)
                print(f"area for width : {width} and height : {length} is: " , area_rectangle ) 
                print(f"environmen for width : {width} and height : {length} is: " ,  environmen_rectangle  )
                agree = str(input("would you like play again?(yes/no)"))
                if agree == "no" :
                    print("Thank you for using our app :)")
            else :
                print("your width or length are invalid.")
            agree = str(input("would you like play again?(yes/no)"))
            if agree == "no" :
                    print("Thank you for using our app :)")
        elif Type_number == 4 :
            square_side = float (input("Please enter square_side:"))        
            if square_side > 0 :
                area_square = area_square (square_side)
                environmen_square = environmen_square(square_side)
                print(f"area for square_side : {square_side} is: " ,  area_square )
                print(f"environment for square_side: {square_side} is: " ,environmen_square )
                agree = str(input("would you like play again?(yes/no)"))
                if agree == "no" :
                    print("Thank you for using my app :)")
            else :
                print("your square_side is invalid.")
            agree = str(input("would you like play again?(yes/no)"))
            if agree == "no" :
                    print("Thank you for using my app :)")    
        elif Type_number == 5 :
            big_side = float(input("Please enter the big_side :"))
            small_side = float(input("Please enter the small_side :"))
            Height = float(input("Please enter the Height:"))
            c_side = float(input("Please enter the c_side:"))
            d_side = float(input("Please enter the d_side:"))
            if c_side and  d_side and big_side and  small_side and Height >0 :
                erea_trapezius = erea_trapezius(big_side , small_side , Height )
                environmen_trapezius = environmen_trapezius(c_side , d_side ,big_side , small_side )
                print("area for the trapezius  is: " , erea_trapezius  )
                print("environment forthe trapezius  is: " , environmen_trapezius)
                agree = str(input("would you like play again?(yes/no)"))
                if agree == "no" :
                    print("Thank you for using my app :)")
            else :
                print("your c_side or d_side or big_side or small_side or Height are invalid.")
                agree = str(input("would you like play again?(yes/no)"))
                if agree == "no" :
                    print("Thank you for using my app :)")
        elif Type_number == 6 :
            a_side = float(input("Please enter the a_side :"))
            b_side = float(input("Please enter the b_side :"))
            c_side = float(input("Please enter the c_side :"))
            d_side = float(input("Please enter the d_side :"))
            a_Diameter = float(input("Please enter the a_Diameter :"))
            b_Diameter = float(input("Please enter the b_Diameter :"))
            if a_side and  b_side and c_side and d_side and a_Diameter and b_Diameter > 0 :
                area_rhombus = area_rhombus(a_Diameter , b_Diameter)
                environmen_rhombus = environmen_rhombus(a_side , b_side , c_side , d_side)
                print("area for the rhombus  is: " ,area_rhombus )
                print("environment forthe rhombus  is: " ,  environmen_rhombus)
                agree = str(input("would you like play again?(yes/no)"))
                if agree == "no" :
                    print("Thank you for using my app :)")
            else :
                print("your a_side or b_side or c_side or c_side or a_Diameter or b_Diameter  are invalid.")
                agree = str(input("would you like play again?(yes/no)"))
                if agree == "no" :
                    print("Thank you for using my app :)")
    else:
        print ("Please enter your desired number from 1 to 6.......")
        agree = str(input("would you like play again?(yes/no)"))
        if agree == "no" :
            print("Thank you for using my app :)")        
         
            
         
            
    
    
    
   
    
       
        
        
        
        


    
          
