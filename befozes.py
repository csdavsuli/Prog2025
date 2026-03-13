uvegek=[5, 2, 2, 4, 3, 2, 4, 10, 5, 5, 3, 5, 4, 3, 3]

def lekvar_mennyiseg():
    
    dl = int(input(f"Mari néni lekvárja (dl): "))
    while dl<0 or dl>200:
        dl = int(input(f"Mari néni lekvárja (dl): "))

    return dl


def legnagyobb_uveg():
    
    maxi = 0
    max_ertek = uvegek[0]
    for i in range(1, len(uvegek)):
        if uvegek[i] > max_ertek:
            max_ertek = uvegek[i]
            maxi = i
    
    return maxi

def ossz_uveg():
    osszeg = 0
    for uveg in uvegek:
        osszeg += uveg

    return osszeg


        
    
#PROGRAM
print(f"2. feladat")
mennyiseg = lekvar_mennyiseg()

print(f"3. feladat")
legnagyobb = legnagyobb_uveg()
print(f"Legnagyobb üveg: {uvegek[legnagyobb]} dl és {legnagyobb+1}. a sorban")

print(f"4.feladat")
meret=ossz_uveg()

if meret > mennyiseg:
    print(f"Elegendő üveg volt.")
    
    i = 0
    while mennyiseg > 0:
        mennyiseg -= uvegek[i]
    
    print(f"Megmaradt üvegek száma: {len(uvegek) -i-1 }")
else:
    print(f"Maradt lekvár!")
    
