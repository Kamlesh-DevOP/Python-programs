item_name=input('Enter the item name: ')
quan=int(input('Enter the quantity: '))
value=int(input('Enter the value: '))
dis=int(input('Enter the discount percent: '))
tax=int(input('Enter the tax percent: '))
amt=quan*value
dis_amt=amt*dis/100
sub_total=amt-dis_amt
grand_total=sub_total+(sub_total*tax/100)
print('*'*10,'BILL','*'*10)

print('Item_name: ', item_name)
print('Discount= ',dis,'%')
print('Tax= ',tax,'%')
print('Subtotal= ',sub_total)
print('Grand total= ',grand_total)
print('*'*26)


