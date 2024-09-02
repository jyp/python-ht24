
gross = 20000
tax_rate_percentage = 30 # int(input("tax?"))
raise_percentage = 3

print(gross)

def actualise(amount, rate, from_year, to):
    for year in range(from_year, to):
        amount = amount + (rate / 100) * amount
        print(year,amount)
    return amount

print(actualise(20000, 3, 2024, 2034) )
# print(gross - ((tax_rate_percentage / 100) * gross))

# salary is 20000
# tax rate is 30%
# what is the net?
