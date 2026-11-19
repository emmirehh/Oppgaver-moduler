#---Snutt 1---
#def lag_hilsen():
#    melding = "Hei!"
#    print(melding)

#lag_hilsen()
#print(melding)                  # Vil gi NameError fordi variabelen melding er definert inne i funksjonen og ikke utenfor, den finnes bare inne i funksjonen, Lokal. 


#---Snutt 2---
#by = "Oslo"

#def skriv_by():
#    print(f"Jeg bor i {by}.")

#skriv_by()                       # Kommer jeg bor i Oslo, fordi variabelen by er definert utenfor funksjonen, og kan leses inne i funksjonen, Global.


#---Snutt 3---
#def doble(tall):
#    tall = tall * 2
#    print(f"Inne: {tall}")

#tall = 5
#doble(tall)
#print(f"Ute: {tall}")            # Kommer Inne: 10. Ute: 5. Inne er lokal, Ute er global. Den lokale variabelen er inne i funksjonen. Den globale variabelen er utenfor funksjonen og blir ikke endret av den lokale variabelen. 


#---Del 2: Poengtelleren---
poeng = 0

def legg_til_poeng():
    poeng += 10

legg_til_poeng()
print(poeng)                      # LocalError, poeng ligger inne i def. 


# Løsning A:
poeng = 0

def legg_til_poeng():
    global poeng
    poeng += 10

legg_til_poeng()
print(poeng)

# Løsning B:
def legg_til_poeng(poeng: int) -> int:
    return poeng + 10 + 25

poeng = 0
poeng = legg_til_poeng(poeng)
print(poeng)


def trekk_fra_poeng(poeng: int, antall: int) -> int:
    return poeng - antall

antall = 5
poeng = 0
poeng = legg_til_poeng(poeng)
antall = trekk_fra_poeng(poeng, antall)
print(antall)


#---Refleksjon---
# I snutt 1 og 3 er variablene inne i funksjonen atskilt fra resten av programmet. I snutt 1 får man error og variabelen er inne i funksjonen. I snutt 3 får man både inne meldingen og ute meldingen. Den globale blir ikke påvirket av den lokale.
# I snutt 2 kunne funksjonen lese by, men i del 2 kunne den ikke endre poeng. Forskjellen kan være at koden tror at det er en ny lokal variabel, derfor må man ha global inne i funksjonen for å finne verdien av poeng.
# Løsning A og B fungerer. De fleste program unngår global, kan motstride hverandre. Kan være vanskelig å følge med og få riktig poensum.