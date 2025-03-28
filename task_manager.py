# Zoznam, kde sa budú ukladať úlohy
ulohy = []

# Funkcia hlavného menu – vráti voľbu používateľa ako text (napr. "1", "2", ...)
def hlavne_menu():
    print("\nSprávca úloh - Hlavné menu")
    print("1. Pridať novú úlohu")
    print("2. Zobraziť všetky úlohy")
    print("3. Odstrániť úlohu")
    print("4. Koniec programu")
    volba = input("Vyberte možnosť (1-4): ")
    return volba

# Funkcia na pridanie novej úlohy
def pridat_ulohu():
    nazov = input("Zadaj názov úlohy: ")
    popis = input("Zadaj popis úlohy: ")
    ulohy.append({"nazov": nazov, "popis": popis})
    print(f"Úloha '{nazov}' bola pridaná.")

# Funkcia na zobrazenie všetkých úloh
def zobrazit_ulohy():
    if len(ulohy) == 0:
        print("Zoznam úloh je prázdny.")
    else:
        print("Zoznam úloh:")
        for poradie, uloha in enumerate(ulohy, start=1):
            print(f"{poradie}. {uloha['nazov']} - {uloha['popis']}")

# Funkcia na odstránenie vybranej úlohy podľa poradia
def odstranit_ulohu():
    if len(ulohy) == 0:
        print("Nie je čo odstrániť. Zoznam je prázdny.")
        return
    
    print("Zoznam úloh:")
    for poradie, uloha in enumerate(ulohy, start=1):
        print(f"{poradie}. {uloha['nazov']} - {uloha['popis']}")
    
    cislo = input("Zadaj číslo úlohy, ktorú chceš odstrániť: ")
    
    if not cislo.isdigit():
        print("Zadal si neplatné číslo.")
        return
    
    index = int(cislo) - 1
    if index < 0 or index >= len(ulohy):
        print("Úloha s takým číslom neexistuje.")
        return
    
    odstranena = ulohy.pop(index)
    print(f"Úloha '{odstranena['nazov']}' bola odstránená.")

# --- HLAVNÝ CYKLUS PROGRAMU ---

# Cyklus sa opakuje, kým používateľ nezvolí možnosť "4"
while True:
    volba = hlavne_menu()

    # Podľa voľby používateľa sa vykoná konkrétna akcia
    if volba == "1":
        print("Zvolil si: pridať úlohu")
        pridat_ulohu()
    
    elif volba == "2":
        print("Zvolil si: zobraziť úlohy")
        zobrazit_ulohy()
    
    elif volba == "3":
        print("Zvolil si: odstrániť úlohu")
        odstranit_ulohu()
    
    elif volba == "4":
        print("Program sa ukončuje...")
        break  # break ukončí while cyklus = program končí
    
    else:
        print("Neplatná voľba. Skús znova.")
