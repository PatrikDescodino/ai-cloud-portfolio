"""

Zadání: "Osobní trenér financí"
Vytvoř funkci financni_trener(), která ti poradí s financemi.
Co má funkce dělat:

Dostane příjmy a seznam výdajů
Spočítá základní statistiky
Vrátí rady na základě analýzy

Konkrétní požadavky:

Pokud ti zbyde víc než 50% příjmu → "Výborně! Můžeš investovat"
Pokud ti zbyde 20-50% → "Dobré hospodaření"
Pokud ti zbyde míň než 20% → "Pozor! Musíš šetřit"
Pokud utrácíš víc než vyděláš → "ALARM! Jdeš do mínusu"

Bonus úkoly (když budeš chtít):

Najdi nejvyšší výdaj a poraď, kde šetřit
Spočítaj, kolik ušetříš za rok
Doporuč konkrétní částku na spoření

"""

# Testovací data:
# Test 1: Šetrný člověk
prijem1 = 40000
vydaje1 = [8000, 2000, 1500, 800]

# Test 2: Rozhazovačný člověk  
prijem2 = 25000
vydaje2 = [15000, 8000, 3000, 2000]

zbytek_Petr = prijem1 - sum(vydaje1)
zbytek_Tomas = prijem2 - sum(vydaje2)

print(f"Petr má zbytek {zbytek_Petr} Kč na účtě!")
print(f"Tomáš má zbytek {zbytek_Tomas} Kč na účtě!")




