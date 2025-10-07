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
#2    

