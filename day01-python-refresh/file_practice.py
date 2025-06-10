# === ČTENÍ A KONTROLA CSV SOUBORU ===
""""
with open('test_data.csv', 'r', encoding='utf-8') as file:
    # Přečti první řádek (hlavičku) ze souboru
    prvni_radek = file.readline().strip()
    
    # Rozděli hlavičku podle čárek na seznam názvů sloupců
    header_nazvy = prvni_radek.split(',')
    
    # Spočítej, kolik sloupců má soubor mít
    pocet_sloupcu = len(header_nazvy)
    
    # Vypiš informace o struktuře souboru
    print("Hlavička:", header_nazvy)
    print("Očekávám", pocet_sloupcu, "sloupců")
    
    # Projdi všechny zbývající řádky v souboru
    for radek in file:
        # Odstraň enter (\n) na konci řádku
        radek = radek.strip()
        
        # Rozděl řádek podle čárek na seznam hodnot
        casti = radek.split(',')
        
        # Zkontroluj, jestli má řádek správný počet sloupců
        if len(casti) == pocet_sloupcu:  # TVŮJ CHYTRÝ ZPŮSOB!
            print("OK řádek:", casti)
        else:
            # Pokud ne, vypiš chybu
            print("CHYBNÝ řádek - má", len(casti), "částí, očekávám", pocet_sloupcu)

# Soubor se automaticky zavře díky 'with'

"""