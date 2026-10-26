poeng = int(input("Hvor mange poeng: "))

if poeng > 100:
    print("Ugyldig")
elif poeng < 0:
    print("Ugyldig")
elif poeng >= 90:
    print("A")
elif poeng >= 80:
    print("B")
elif poeng >= 60:
    print("C")
elif poeng >= 50:
    print("D")
elif poeng >= 40:
    print("E")
else:
    print("F")


#---Refleksjon---
# Jeg tror 95 blir A. 72 blir C. 40 blir E. 12 blir F. Alle stemte.

# Dersom man snur rekkefølgen med at man sjekker E først, vil 95 poeng gi "E" i stedetfor "A", siden det er den som blir sjekket først og oppfyller kravene.
# Dersom man tar flere if etter hverandre i stedet for if og elif, skriver den ut alle if statementene. If er hvis. Elif er ellers hvis.
# Vi trenger ikke å sjekke om poengene også er under 90 fordi kravet over allerede er oppfylt.
# Koden i Else blokken kjører hvis ingen av de foregående betingelsene treffer.