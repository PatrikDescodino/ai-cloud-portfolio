prijmy = 35000
vydaje = {
    "cena": [8000, 3000, 2500, 1200, 800],
    "nazvy": ["nájem", "jídlo", "doprava", "telefon", "zábava"]
}

print("Můj měsíční příjem je", prijmy, "Kč")
print("Můj největší výdaj je", vydaje["cena"][0], "Kč a je to za", vydaje["nazvy"][0])


celkove_vydaje = sum(vydaje["cena"])
zustatek = prijmy - celkove_vydaje

print("Celkove vydaje:", celkove_vydaje, "Kč")
print("Zbývá mi: ", zustatek, "kč")

# --- cycle --- #
print("\n--- DETAIL VŠECH VÝDAJŮ ---")
for i in range(len(vydaje["cena"])):
    cena = vydaje["cena"][i]
    nazev = vydaje["nazvy"][i]
    print(f"{nazev}: {cena} Kč")


def spocitej_naklady(prijmy, vydaje_seznam):
    """Spočítá zůstatek z příjmů a výdajů"""
    celkove_vydaje = sum(vydaje_seznam)
    zbytek = prijmy - celkove_vydaje
    return zbytek  # Vrátí výsledek

# Použití
muj_prijem = 35000
moje_vydaje = [8000, 3000, 2500, 1200, 800]

vysledek = spocitej_naklady(muj_prijem, moje_vydaje)
print(f"Zbývá mi: {vysledek} Kč")

# Můžu to použít i v dalších výpočtech
if vysledek > 10000:
    print("Můžu si dovolit dovolenou!")
else:
    print("Musím šetřit...")


# Pokud někdy možná budeš potřebovat výsledek → return
# Pokud jen chceš něco ukázat → print