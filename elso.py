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

tipp=(input("Kérek egy számot 1 és 100 között: "))
while (not tipp.isdecimal()):
    print("Nem számot adtál meg,egész számot adj meg")
    tipp=(input("Kérek egy számot 1 és 100 között: "))

    
tipp=int(tipp)
    
if (tipp<kszam):
    print("A keresett szám nagyobb")
elif (tipp>kszam):
    print("A keresett szám kisebb")




if (tipp<kszam):
    print("A keresett szám nagyobb")
elif(tipp>kszam):
    print("A keresett szám kisebb")
while(tipp!=kszam):
    tipp=(input("Kérek egy számot 1 és 100 között: "))
    while (not tipp.isdecimal()):
        print("Nem számot adtál meg,egész számot adj meg")
        tipp=(input("Kérek egy számot 1 és 100 között: "))

    tipp=int(tipp)
    
    if (tipp<kszam):
        print("A keresett szám nagyobb")
    elif (tipp>kszam):
        print("A keresett szám kisebb")
print("Eltaláltad a számot")