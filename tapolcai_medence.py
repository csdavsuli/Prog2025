szoveg = ""

mondatvegi = ['.', '?', '!']
try:
    with open("leiras.txt", encoding="utf-8") as fajl:
        szoveg = fajl.read()
        
    
except IOError as ex:
        print(f"IO hiba {ex}")
        
def cim_formazas():
    sorok = szoveg.split('\n')
    
    for i in range(len(sorok)):
        if sorok[i][-1] not in mondatvegi:
            sorok[i] = f"\n{sorok[i]}\n{'-'*len(sorok[i])}\n"
    
    ujszoveg = "\n".join(sorok)    
    
    print(ujszoveg)  
    
    try: 
        with open("uj_leiras.txt","w", encoding="utf-8") as fajl:
            fajl.write(ujszoveg)
    except IOError as ex:
        print(f"IO hiba {ex}")
    
    
def mondat_szavak_szama():
    mondatszam = szoveg.count('.')
    mondatszam += szoveg.count("!")
    mondatszam += szoveg.count(" ? ")
    
    print(f"A szövegben lévő mondatok száma: {mondatszam}")
    





########################

cim_formazas()