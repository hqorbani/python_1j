print("the menu:")
print("peperoni : 5$")
print("mix : 4$")
print()
pizza =input(" choose your  pizza:").lower()
number =int(input("please enter number of your pizza:"))
if number > 0 :
    if pizza =="peperoni"  :
        print('amount:', number*5)
    elif pizza == "mix"  :
        print("amount:",number*4) 
    else :
        print("Until further notice, we only have pizza:)" )
else :
    print('Please use positive integers..')        



