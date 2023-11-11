import pickle,os
with open("fff.dat", "wb") as f:
    for i in range(3):
        ide = int(input("Enter ID: "))
        nam = input("Enter name: ")
        sal = int(input("Enter salary: "))
        exp= int(input('Enter experience: '))
        pickle.dump({ide:[nam,sal,exp]},f)

with open('fff.dat','rb') as f, open('temp.dat','wb') as f1:
    try:
        while True:
            d=pickle.load(f)
            for key in d:
                if d[key][2]>=5:
                    pickle.dump(d,f1)
    except:
        pass
    os.remove('fff.dat')
    os.rename('temp.dat','fff.dat')
