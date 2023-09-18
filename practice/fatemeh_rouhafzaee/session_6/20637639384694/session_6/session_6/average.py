numbers = [154,322,21,64,233,125,24]
number = []
for item in numbers :
    if item % 3 == 0 :
      number.append(item)
if len(number) > 0:
   print(sum(number) / len(number))
else:
   print("I did not find any number for result")

