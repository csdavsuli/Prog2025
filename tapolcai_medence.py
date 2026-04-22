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
    
    mondat_lista = szoveg.split('\n')
    
    szavak_szama=0
    for mondat in mondat_lista:
        szavak_szama += len(mondat.split())

    print(f"A szövegben lévő szavak száma: {szavak_szama}")

def hegyek(szoveg):
    hegyek_lista = []

    szoveg = szoveg.replace('\n',' ')
    szavak_lista = szoveg.split()
    
    for szo in szavak_lista:
        if "HEGY" in szo.upper():
            szo = szo.strip(',').strip('.').strip('!')
            if szo not in hegyek_lista:
                hegyek_lista.append(szo)
    print(f"Hegyek:\n\t{hegyek_lista}")
"""    
def szocsere(szoveg):

szoveg= szoveg.replace('Balaton', 'BALATON')
szoveg = szoveg.replace('vulkán', 'tűzhányó')    
"""

def min_max_maganhangzo(szoveg):
    maganhangzok = "aáeéiíoóöőuúüű"
    maganhangzo_db = []
    
    
    for i in range(len(maganhangzok)):
        maganhangzo_db.append(szoveg.count(maganhangzok[i]))
            
    print(maganhangzo_db)
    
    mini = 0
    maxi = 0
    
    for i in range(1, len(maganhangzo_db)):
        if  maganhangzo_db[i] < maganhangzo_db[mini]:
            mini=i
        if maganhangzo_db[i] > maganhangzo_db[maxi]:
            maxi=i
    print(f"A legritkábban előforduló magánhangzó: {maganhangzok[mini]}")
    print(f"A leggyakrabbban előforduló mássalhangzó: {maganhangzok[maxi]}")

def tomorito(szoveg):
    maganhangzok = "aáeéiíoóöőuúüű"
    tomoritett = szoveg
    for mghg in maganhangzok:
        tomoritett = tomoritett.replace(mghg, '')

    print(f'\nEredeti: {szoveg[0:80]}\n')
    print(f"Tömörített:{tomoritett}")
########################

cim_formazas()
mondat_szavak_szama()
hegyek(szoveg)
#szocsere(szoveg)
min_max_maganhangzo(szoveg)
tomorito(szoveg)