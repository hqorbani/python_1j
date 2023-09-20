numbers = [1,2,3,21,51,68,59,53,654,21,57]
for i in range(0,len(numbers)) :
    group = numbers[i:i+3]
    if len(group) == 3 :
        print(group)
