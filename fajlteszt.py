#fajl=open("F1-2024dec.csv", encoding="utf-8")
#sz = fajl.read()
#sz1=fajl.read(150)
#sz1=fajl.readlines()

#print(sz)
#print(f"\n----\n{sz1}")
#print(f"\n{sz1}")
try:
    with open("F1-2024dec.csv", encoding="utf-8") as fajl:
        f=fajl.read()
        n=4/0
        
        print(f)
        print(n)


except Exception as e:
    print("Hiba történt:", e)    

except FileNotFoundError:
    print("Nincs ilyen fájl")   
except ZeroDivisionError:
    print("Nullával osztás hiba")

print ("itt a vége")

fajl.close()
