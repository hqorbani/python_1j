numbers = [154,321,12,23,35,63,230,251,21,238,659,250,522,2541,12,10,19,18]
number_greater_than_100 = []
number_smaller_than_100 = []
for items in numbers :
    if items > 99 :
     number_greater_than_100.append(items)
    elif items < 101 :
     number_smaller_than_100.append(items)    
    print("number_greater_than_100: " , len(number_smaller_than_100))
    print("number_smaller_than_100: " , len(number_smaller_than_100))   
    print("average_greater_than_100: " , sum(number_smaller_than_100)/len(number_smaller_than_100))
    print("average_smaller_than_100: " , sum(number_smaller_than_100)/len(number_greater_than_100))

 
    
