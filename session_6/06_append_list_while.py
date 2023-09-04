names = []
counter = 1
while counter <= 5:
    name = input("please enter new name: ")
    names.append(name)
    counter = counter + 1
    counter += 1
for item in names:
    print(item)