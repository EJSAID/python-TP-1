note1= float(input("saisir la note 1:"))
note2=float(input("saisir la note 2 :"))
note3=float(input("saisir la note 3:"))



def calculmoy(note1,note2,note3):
     if 0 <= note1 <= 20 and 0 <= note2 <= 20 and 0 <= note3 <= 20:
          return (note1 + note2 + note3) / 3
  


moy=calculmoy( note1, note2, note3)
print("le moyenne est : "+ moy)

if moy < 10:
    print("insuffisant en dessous de 10")
elif moy >= 10 and moy <12 : print("passable")
elif moy >= 12 and moy <14 : print ("assez bien")
elif moy >= 14 and moy <16 : print ("bien")
elif moy>=16 : print ("trés bien")






