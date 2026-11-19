def regn_pris(antall, pris_per_stk):
    return antall * pris_per_stk

def skriv_kvittering(navn, total):
    print(f"Kvittering for {navn}")
    print(f"Totalt: {total} kr")

def avslutt():
    print("Takk for handelen!")

pris = regn_pris(3, 49.90)
total = pris
skriv_kvittering("Michael", pris)
print(f"Du betalte {total} kr.")
avslutt()


#---Refleksjon---
# Feilene var: Manglet kolon etter den første def. Manglet innrykk på den første print linjen i den andre def. Manglet () i avslutt. Manglet return i linje 2. De glemte også å definere pris utenfor.
# 2 feil som ikke ga feilmelding: Avslutt ga ikke feilmelding, så det kom ikke takk for handelen. Den andre var 
# Rettet linjen med total med å definere totalen som pris.
# print(avslutt) uten paranteser så kommer det error. Dersom man skriver avslutt uten paranteser som det først var i koden, blir ikke noe printet før man legger til parantesene.
