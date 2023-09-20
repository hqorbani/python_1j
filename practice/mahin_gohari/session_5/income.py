fund = 4000
month = 1 
while month < 12:
    income = fund * 10 / 100 + fund
    fund = income
    month += 1
    want = 30 * fund / 100
    need = 50 * fund / 100
    money = 20 * fund / 100
    print(want , need , fund)
