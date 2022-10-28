weight=int(input('enter the parcel weight in gram'))
additional_weight=weight-1000
#fixed_weight=1000
fixed_amt=15

x=additional_weight/500
additional_amt=x*8
print('Total charge is ',additional_amt+fixed_amt)