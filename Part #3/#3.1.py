def cash(deposit, percent, year):
    profit = (deposit * percent * year) / 100
    real_cash = deposit + profit
    return real_cash

