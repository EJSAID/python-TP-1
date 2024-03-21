age = int(input("saisir votre age svp :"))
sexe = input("saisir votre sexe svp :")


if age >=20 and sexe == 'H':
    print("Cet habitant doit payer l'impôt.")
elif 18>= age <=35 and sexe == 'F':
    print("Cet habitant doit payer l'impôt.")
else :
    print("Cet habitant ne doit pas payer l'impôt.")
