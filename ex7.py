nbr = int(input("entrer un nombre entier :"))
s=0

if nbr < 0:
    print("sasir un nombre entiersvp")
else:
    for i in range(1,nbr+1):
        s = s+i**2


print(s)