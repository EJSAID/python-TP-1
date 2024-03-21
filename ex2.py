import math

def resoudre_equation_second_degre(a, b, c):
   
    discriminant = b**2 - 4*a*c
    
    # Cas où le discriminant est positif
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return "Deux solutions réelles :", x1, "et", x2
    
    # Cas où le discriminant est nul
    elif discriminant == 0:
        x = -b / (2*a)
        return "Une solution réelle double :", x
    
    # Cas où le discriminant est négatif (racines complexes)
    else:
        partie_reelle = -b / (2*a)
        partie_imaginaire = math.sqrt(abs(discriminant)) / (2*a)
        return "Deux solutions complexes :", complex(partie_reelle, partie_imaginaire), "et", complex(partie_reelle, -partie_imaginaire)

# Exemple d'utilisation de la fonction
a = 1
b = -3
c = 2

solutions = resoudre_equation_second_degre(a, b, c)
print(solutions)
