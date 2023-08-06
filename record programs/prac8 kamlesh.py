category = ["SENIORS", "JUNIORS", "SUBJUNIORS"]
houses = ["BHARATHI","TAGORE", "SHIVAJI", "PRATAP"]
score = dict()
for i in category:
    print(i)
    temp = {}
    for j in houses:
        pt = int(input(f'Enter points of {j}: '))
        temp[j] = pt
    score[i] = temp
print()
def MAX_SCORE(D):
    for category in D:
        d=D[category]
        max=0
        winner=None
        print(category)
        for house in d:
            if d[house]>max:
                max=d[house]
                winner=house
        print(winner,max)
        print()
MAX_SCORE(score)