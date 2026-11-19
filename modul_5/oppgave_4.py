#--- Del 1: Karakterkalkulatoren---
def finn_karakter(poeng: int) -> str:
    if poeng > 100:
        return ("Ugyldig")
    elif poeng < 0:
        return ("Ugyldig")
    elif poeng >= 90:
        return ("A")
    elif poeng >= 80:
        return ("B")
    elif poeng >= 60:
        return ("C")
    elif poeng >= 50:
        return ("D")
    elif poeng >= 40:
        return ("E")
    else:
        return ("F")

#finn_karakter(75)


def skriv_resultat(navn: str, karakter: str) -> None:
    print(f"Navn: {navn}, Karakter: {karakter}.")

navn = input("Navn: ")
karakter = finn_karakter (int(input("Poeng: ")))
skriv_resultat(navn, karakter)


#--- Del 2: Hva typehint ikke gjør---
def doble(tall: int) -> int:
    return tall * 2

print(doble("5"))         # Trodde det ble 5. Det ble 55. Den doblet det som sto i str, la til en til 5.


brus = 24.90
smørbrød = 45
banan = 8.50

def regn_total(brus: float, smørbrød: float, banan: float) -> float:
    return brus + smørbrød + banan

total = regn_total(brus, smørbrød, banan)
print(total)


def legg_til_mva(regn_total: float) -> float:
    return total * 1.25                         # Man trenger kun å endre her dersom mvaen endrer seg.

mva = legg_til_mva(regn_total)
print(mva)


def del_regning(mva: float) -> float:
    return mva / 4

delt_regning = del_regning(mva)
print(delt_regning)


#---Refleksjon---
# Den gamle karakterkalkulatoren er den letteste å lese fordi man ikke trenger en ekstra prosedyre for å printe den ut.
# Fikk riktig svar i steg 4 uten elif fordi seperate if statementene er innenfor funksjonen, så det blir lest som en samla statement.
# Python stoppet ikke i del 2. Typehint forteller hvilke datatyper en funksjon forventer og gir tilbake. Den blir mer lesbar og mindre gjetning.