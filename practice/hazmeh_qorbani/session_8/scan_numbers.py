numbers = [1,2,3,21,51,68,59,53,654,21,57]
index , roof = 0 , 0
period = 3
sum = 0
scan_list = []
while index < len(numbers):
    roof = index + period
    index_2 = index
    while index_2 < roof:
        scan_list.append(numbers[index_2])
        index_2 += 1
    index += 1
    print(scan_list)
    scan_list = []
