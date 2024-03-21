nb1= float(input("saisir un nombre :"))
nb2 = float(input("saisir un deuxieme nombre :"))
operator= input("saisir un operator :")

if operator=='+':
   print(nb1+nb2)
elif operator=='-':
     print(nb1-nb2)
elif operator=='*':
     print(nb1*nb2)
else :
    if nb2>0:
        print(nb1/nb2)
    else :
        print(error)
