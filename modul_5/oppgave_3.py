def doble_print(tall):
    print(tall * 2)

def doble_return(tall):
    return tall * 2
    print("ferdig!")    # Blir ikke skrevet ut.

doble_print(5)          # Ble 10. 5 * 2 = 10.
doble_return(5)


a = doble_print(5)   
b = doble_return(5)  
print(a)             # a blir None, kan ikke ta med seg verdien fra tidligere.
print(b)             # b blir 10.

print(doble_return(5) + 1)     # Blir 11.
#print(doble_print(5) + 1)     # Fungerte ikke, kunne ikke gjenbruke verdien.

print(doble_return(doble_return(3)))    # Blir 12. Dobler den første, så dobler den på nytt igjen.


def regn_areal(lengde, bredde):
    return lengde * bredde

def skriv_areal(lengde, bredde):
    print(f"Areal: {lengde * bredde}.")

c = regn_areal (2, 10)
print(c)
skriv_areal(2, 10)



#---Refleksjon---
# Ingenting ble skrevet ut fra doble_return(5) fordi den prosedyren ikke sier at den skal printe det, den tar imot verdien, men sier ikke print.
# A i steg 3 var None. Denne verdien betyr at når man ikke bruker return kan man ikke bruke verdien i en ny variabel. 
# Steg 6 sier at return gjenbruker verdier, print gir ikke verdier, men printer.
# Prosedyre (som gjør noe), skriver ut tekst. Funksjon (som gir tilbake en verdi) med return, den verdien kan du lagre i en variabel og bruke videre.