from itertools import permutations 


Fichas = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]

M1 = []
M2 = []
M3 = []
M4 = []
MF = []


#for f in range (28):

    #print (f)

perm = permutations(Fichas)

for i in list(perm): 

    #print (i) 

    #if i == 30 return
    
    for f in range(0,7):

        M1.append (f)
        #print (f)

    for f in range(7,14):

        M2.append (f)
        #print (f)

    for f in range(14,21):

        M3.append (f)
        #print (f)

    for f in range(21,28):
        
        M4.append (f)
        #print (f)


#print (M1)
#print (M2)
#print (M3)
#print (M4)

MF = M1 + M2 + M3 + M4

print (MF)


#return
