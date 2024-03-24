s=0
terme=""
n = int(input("entrer un nombre entier :"))
for i in range(n+1):
    s+=10**i
    terme += str(10 ** i)
    if i < n:
      terme += " + "
print("s=",terme)