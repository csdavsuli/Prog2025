#fajl=open("F1-2024dec.csv", encoding="utf-8")
#sz = fajl.read()
#sz1=fajl.read(150)
#sz1=fajl.readlines()

#print(sz)
#print(f"\n----\n{sz1}")
#print(f"\n{sz1}")

verseny_adatok=[]
try:
    with open("F1-2024dec.csv", encoding="utf-8") as fajl:
        verseny_adatok=fajl.readlines()


except Exception as e:
    print("Hiba történt:", e)    
 
except FileNotFoundError:
    print("Nincs ilyen fájl")   
except ZeroDivisionError:
    print("Nullával osztás hiba")
print(verseny_adatok)
print ("itt a vége")


"""
1   []Megszámlálás
2   []Eldöntés
    []Eldöntés 2
3   []Kiválasztás
4   []Keresés  
5   []Sorozatszámítás
6   []Minimum, maximum kiválasztás
    
7   []Másolás
8   []Kiválogatás
9   []Szétválogatás
10  []Metszet
11  []Únió
12  Rendezés  
    []Egyszerű cserés rendezés
    []Buborékos rendezés
    []Minimum kiválasztásos rendezés
"""
#1. feladat: Hány versenyző nem szerzett még ponotot?
db=0
for i in range(1,len(verseny_adatok)):
    if int(verseny_adatok[i].split(",")[1]=="0"):
        db+=1

print(f"1. feladat: {db} versenyző nem szerzett pontot.")
#2 Van-e Fernando nevű versenyző?
i=0
while i<len(verseny_adatok) and "Fernando" not in verseny_adatok[i] :
    i+=1
if i<len(verseny_adatok):
    print("2. feladat: Van Fernando nevű versenyző.")
else:
    print("2. feladat: Nincs Fernando nevű versenyző.")
#Eldöntés 2
#3. feladat: Mndenkit szerzett már 90 pontot?
i=1
while i<len(verseny_adatok) and int(verseny_adatok[i].split(",")[1])>=90:
    i+=1
if i==len(verseny_adatok):
    print("3. feladat: Mindenki szerzett már 90 pontot.")
else:
    print("3. feladat: Nem mindenki szerzett még 90 pontot.")
    
#4. feladat: Ki istálló pilótája Yuki Tsunoda?
i=0
while verseny_adatok[i].split(",")[0]!="Yuki Tsunoda":
    i+=1
print(f"4. feladat: Yuki Tsunoda istállója: {verseny_adatok[i].split(',')[2]}")

#5.feladat Melyik csapatban volt Pierre Gasly?
i=1
while i<len(verseny_adatok) and "Pierre Gasly" not in verseny_adatok[i]:
    i+=1
if i<len(verseny_adatok):
    print(f"5. feladat: Pierre Gasly csapata: {verseny_adatok[i].split(',')[2]}")
else:
    print("5. feladat: Nincs Pierre Gasly nevű versenyző.")

#6.feladat: Számoljuk a pontok átlagát!
S=0
for i in range(1,len(verseny_adatok)):
    S+=int(verseny_adatok[i].split(",")[1])
print("6. feladat: A pontok átlaga:", S/len(verseny_adatok)-1)

#7.feladat
maxi=1
max=verseny_adatok[1].split(",")[1]
for i in range(3,len(verseny_adatok)):
    if verseny_adatok[i].split(",")[1]>max:
        max=int(verseny_adatok[i].split(",")[1])
        maxi=i


#9.feladat: Kiválogatás kigyyűjtéssel Kik vannak a mclaren csapatában?
db1=1
listamc=[]
for i in range(1,len(verseny_adatok)):
    if verseny_adatok[i].split(",")[2].strip()=="McLaren":
        db1+=1
        listamc.append(verseny_adatok[i].split(",")[0])
        
print   (f"9. feladat: A McLaren csapatában {db1} versenyző van.")

#szétválogatás
dby=0
dbx=0
y=[]
x=[]
for i in range(1,len(verseny_adatok)):
    if int(verseny_adatok[i].split(",")[1].strip()!=0):
        dby+=1
        y.append(verseny_adatok[i].split(",")[0])
    else:
        dbx+=1
        x.append(verseny_adatok[i].split(",")[0])
print(f"10. feladat: {dby} versenyző szerzett pontot ők: {y}, {dbx} versenyző nem szerzett pontot ők: {y}.")

#rendezés minimum kiválasztásos rendezés pontok szerint növekvő sorrendbe
for i in range(1,len(verseny_adatok)-1):
    mini=i
    min=int(verseny_adatok[i].split(",")[1])
    for j in range(i+1,len(verseny_adatok)):
        if int(verseny_adatok[j].split(",")[1])<int(verseny_adatok[mini].split(",")[1]):
            mini=j
            min=int(verseny_adatok[j].split(",")[1])
    verseny_adatok[i], verseny_adatok[mini]=verseny_adatok[mini], verseny_adatok[i]

print("11. feladat: Rendezett lista pontok szerint növekvő sorrendben:")
for i in verseny_adatok:
    print(i.strip())