n = int(input("entrer un nombre entier :"))
s=0
for i in range(1,n):
    if n%i ==0:
        s+=i
  

if s==n:
      print(str(n)+" est une nombre parfait")
else:
        print(str(n)+" est pas une nombre parfait")
