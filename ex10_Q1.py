tab=[]
i=0
for i in range(10):
    element=int(input("entrer element "+str(i + 1)+" de tableau :"))
    tab.append(element)

croissant=True

for i in range(len(tab)-1):
    if tab[i] > tab[i+1]:
        croissant=False
    break

if croissant:
    print ("le tableau est trié dans un ordre croissant")
else:
    print ("le tableau est trié dans un ordre non croissant")



