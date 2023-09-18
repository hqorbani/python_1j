height = float(input("please enter your height (kg) : "))
Weight = float(input("please enter your Weight (m) : "))
bmi = round(height / Weight ** 2 , 1)
if bmi < 18.5 :
    print ("your BMI index is :" , bmi ,  "Underweight")
elif  18.5 < bmi < 24.9 :
    print("your BMI index is :" , bmi ,   "normal")   
elif  25 < bmi < 29.9 :
    print("your BMI index is :" , bmi ,   "Overweight")
elif 30 < bmi < 34.9 :
    print ("your BMI index is :" , bmi ,   "Excessive weight gain")
elif 35 < bmi :
    print("your BMI index is :" , bmi ,   "excessive obesity")