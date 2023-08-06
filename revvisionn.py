import pickle
def view():
    c=0
    with open('abc.dat','rb') as f:
        try:
            while True:
                l=pickle.load(f)
                print(l)
                c+=1
        except:
            return c

print(view())