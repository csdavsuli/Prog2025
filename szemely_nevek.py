"""
NÉVKEZELŐ PROGRAM
"""


# ============================================================================
# 1. FELADAT: Szövegfájl tartalmának beolvasása
# ============================================================================

def nevek_betoltese(fajlnev):
    """
    Feladat: Olvasd be a neveket a szemely_nevek.txt fájlból egy listába!
    
    A fájl minden sorában egy név szerepel (pl. "András Kovács").
    
    Paraméterek:
        fajlnev (str): A beolvasandó fájl neve
    
    Visszatérési érték:
        lista: A neveket tartalmazó lista
    """
    # TODO: Implementáld a fájlbeolvasást
    try:
        with open(fajlnev, encoding="utf-8") as fajl:
            nevek=fajl.readlines()
            
            return nevek
        
    except IOError as ex:
        print(f"IO hiba:{ex}")     


# ============================================================================
# 2. FELADAT: Egyedi keresztnevek kigyűjtése
# ============================================================================

def keresztenevek_gyujtese(nevek):
    """
    Feladat: Gyűjtsd ki az összes (első) keresztnevet!
    
    Példa: ["András Kovács", "Anna Mária Szabó"] -> ["András", "Anna"]
    
    Paraméterek:
        nevek: A nevek listája
    
    Visszatérési érték:
        lista: Az egyedi keresztnevek listája
    """
    # TODO: Implementáld a függvényt
    keresztenevek = []
    
    for nev in nevek:
        keresztnev=nev.split(' ')[0]
        
        if keresztnev not in keresztenevek:
            keresztenevek.append(keresztnev)
    
    return keresztenevek
        
        



    


# ============================================================================
# 3. FELADAT: Leggyakoribb családnév
# ============================================================================

def leggyakoribb_csaladnev(nevek):
    """
    Feladat: Határozd meg, melyik a leggyakoribb családnév!
    
    A megoldás során tárold el egy külön listában a családneveket és azok gyakoriságát!
    
    Példa: ["András Kovács", "Anna Szabó", "Balázs Kovács"] 
            -> csaladnevek: [
                             ["Kovács", 2],
                             ["Szabó", 1]
                            ]
    
    Paraméterek:
        nevek: A nevek listája
    
    Visszatérési érték:
        string: a leggyakoribb családnév
    """
    # TODO: Implementáld a függvényt
    csaladnevek = []
    for nev in nevek:
        csaladnev=nev.split()[-1]
        
        if csaladnev not in csaladnevek:
            csaladnevek.append(csaladnev, 1)
    
    return csaladnevek

# ============================================================================
# 4. FELADAT: Nevek "magyarosítása"
# ============================================================================

def nevek_megforditasa(nevek):
    """
    Feladat: Cseréld meg a kereszt- és családnevek sorrendjét, hogy a magyar névhasználatnak megfelelő legyen!
    
    Példák:
        "András Kovács" -> "Kovács András"
        "Anna Mária Szabó" -> "Szabó Anna Mária"
    
    Paraméterek:
        nevek: Az eredeti nevek listája
    
    Visszatérési érték:
        lista: A megfordított nevek listája
    """
    # TODO: Implementáld a függvényt
    pass





# ============================================================================
# FŐPROGRAM
# ============================================================================

def main():
    
    print("=" * 60)
    print("NÉVKEZELŐ PROGRAM - FÜGGVÉNYEK TESZTELÉSE")
    print("=" * 60)
    
    
    # =====================================================
    # 1. FELADAT: Szövegfájl tartalmának beolvasása
    # =====================================================
    # TODO: Hívd meg a nevek_betoltese() függvényt a "nevek.txt" fájllal 
    nev_lista = nevek_betoltese("szemely_nevek.txt")
    print(nev_lista)
    
    # =====================================================
    # 2. FELADAT: Egyedi keresztnevek kigyűjtése
    # =====================================================
    # TODO: Hívd meg a keresztenevek_gyujtese() függvényt
    # és írasd ki az eredményt
    keresztnev_lista = keresztenevek_gyujtese(nev_lista)
    print(keresztnev_lista)
    
    # =====================================================
    # 3. FELADAT: Leggyakoribb családnév
    # =====================================================
    # TODO: Hívd meg a leggyakoribb_csaladnev() függvényt
    # és írasd ki az eredményt    
  
    
    # =====================================================
    # 4. FELADAT: Nevek "magyarosítása"
    # =====================================================
    # TODO: Hívd meg a nevek_megforditasa() függvényt
    # és írasd ki az eredményt
    
    

    
    print("\n" + "=" * 60)
    print("PROGRAM VÉGE")
    print("=" * 60)


# ============================================================================
# PROGRAM INDÍTÁSA
# ============================================================================

if __name__ == "__main__":
    main()


