def skriv_velkomst():
    print("Velkommen!")
    print("Dette er menyen vår")

def skriv_skillelinje():
    print("-" * 20)

def skriv_meny():
    skriv_skillelinje()
    print("---Meny---")
    print("1. Pizza")
    print("2. Burger")
    print("3. Salat")
    skriv_skillelinje()

skriv_velkomst()
skriv_meny() # Koden i prosedyren kjører ikke før man kaller på den, ved å skrive navnet med paranteser.
             # Det kommer Error dersom man ikke har innrykk på printen inne i prosedyren.
skriv_meny()
skriv_meny() 

#---Refleksjon---
# Når man kaller skillelinjen inne i menyen, vil det komme en skillelinje før og etter menyen. 
# Steg 1: Prosedyren definerer hva som skal skje når man kaller på den, men koden inne i prosedyren kjører ikke før man kaller på den.
# Ved å definere en prosedyre skriver man hva den samlende navngittekoden skal være, mens det å kalle på en prosedyre vil si at man ønsker å kjøre koden som er definert i prosedyren, det kan man gjøre flere ganger i koden.
# Det kommer Error NameError dersom man prøver å kalle på en prosedyre som ikke er definert. Python leser koden fra toppen til bunnen.
# Det kan være nyttig å samle kode i en prosedyre for å gjøre koden mer oversiktlig, lettere å lese og man slipper å skrive samme kode flere ganger. Dersom man må skrive de samme print linjene flere ganger er det også større fare for skrivefeil.