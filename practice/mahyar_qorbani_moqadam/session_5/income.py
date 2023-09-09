income = 4000
month = 1
while month <= 12:
    month += 1
    income = 4000 * 10 / 100 +  income
    need = 50 * income / 100
    want = 30 * income / 100
    increase = 20 * income / 100
    income = increase + income
    print("inncome:" , income , "need:" , need , "want:" , want)
print("finished")    