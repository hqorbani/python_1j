numbers = [154,321,12,23,35,63,230,251,21,238,659,250,522,2541,12,10,19,18]
number = []
for items in numbers :
    if items / 3 == 0 :
      number.append(items)
print(sum(number) / len(number))    
