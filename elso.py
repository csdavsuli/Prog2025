import random


szamok=[]

#100 elemű lista feltöltése 1-999 közötti véletlen számok

#szám generálás

for i in range(100):
    szam=random.randint(0,100)
    szamok.append(szam)

print(szamok)

#kitalálandó szám beállítása
kszam=szamok[random.randint(0,len(szamok))]

tipp=int(input("Kérek egy számot 1 és 100 között: "))
if (tipp==kszam):
        print("Gratulálok, eltaláltad a számot")
elif (tipp<kszam):
    print("A keresett szám nagyobb")
else:
    print("A keresett szám kisebb")
while(tipp!=kszam):
    tipp=int(input("Kérek egy számot 1 és 100 között: "))
    if (tipp==kszam):
        print("Gratulálok, eltaláltad a számot")
    elif (tipp<kszam):
        print("A keresett szám nagyobb")
    else:
        print("A keresett szám kisebb")