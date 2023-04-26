f=open('covid.txt','w')
f.write('''c''')
f.close()

f2=open('edited.txt','w')
f1=open('covid.txt')
textlist=f1.readlines()
for line in textlist:
    for word in line.split():
        if 'covid' in word:
            f2.write('COVID-19 ')
        else:
            f2.write(word+' ')
    f2.write('\n')
f1.close()
f2.close()