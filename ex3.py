temp = int(input("saisir un Temp en seconds svp: "))


heures = temp // 3600
minutes_restantes = temp % 3600
minutes = minutes_restantes // 60
secondes = minutes_restantes % 60

resultat = str(heures) + " heures " + str(minutes) + " minutes " + str(secondes) + " secondes."
print(resultat)