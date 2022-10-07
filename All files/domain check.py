from xml import dom


st=input('Enter a email id: ')
domain='@gmail.com'
len_do=len(domain)
domain_start_index=len(st)-len_do
domain_part=st[domain_start_index:]
if domain_part==domain:
    print('It belongs to our domain')
else:
    print('It does not belong to our domain')
    


