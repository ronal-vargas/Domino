from itertools import combinations

def perm1(lst):
#    if len(lst) == 0:
#        return[]
#    elif len(lst) == 1:
#        return [lst]
#    else:
        l = []
        for i in range(len(lst)):
            x = lst[i]
            xs= lst[:i] + lst[i+1:]
            for p in perm1(xs):
                l.append([x]+p)
        return l

#data = list('abc')
data = [1,2,3]
#print perm1
for p in perm1(data):
    print (p)



numeros = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
#numeros = [1,2,3]

for c in combinations(numeros,28):

    print (c)