income=int(input('Enter your salary: '))
taxable_income=income-150000
if taxable_income<=0:
    print('No tax!')
elif taxable_income>150001 and income<300000:
    tax=(taxable_income-150001)*0.1
elif taxable_income>300001 and taxable_income<500000:
    tax=(taxable_income-300001)*0.2
else:
    tax=(taxable_income-500001)*0.3
print('Tax: ',tax)
