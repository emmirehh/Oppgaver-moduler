navn = input("Hva heter du: ")
print("Hei,", navn)

print(f"Hei, {navn}!")

alder = input("Hvor gammel er du: ")
print(type(alder)) # Datatypen er string.

# print(alder + 1) # TypeError: can only concatenate str (not "int") to str.

alder = int(alder)
print(type(alder)) # Datatypen er blitt gjort om til integer.
print(f"Du blir {alder + 1} til neste år!")

høyde = input("Hvor høy er du i meter: ")
# høyde = int(høyde), kommer feilmelding, siden høyden må stå som desimaltall (float) og ikke heltall (integer).
høyde = float(høyde)
print(f"Du er {høyde} meter høy!")


#---Refleksjon---
# Dersom man bruker int på høyden, kommer det en feilmelding, siden desimaltall er float og heltall er integer, forskjellige datatyper. String var datatypen på alderen før jeg brukte int(). input gir string fordi programmet ikke vet hva brukeren kommer til å skrive, tall kan også leses som tekst.
# I steg 5 klaget Python på at den ikke kan blande datatype str og int.
# Med f-string blir koden kortere og lettere å lese. Kalle på logikk i print statementen. Kombinere teskt med variabler, og setter verdien rett inn i teksten. I den første fungerer kommaet som et skille mellom ledeteksten og variabelen, 2 forskjellige ting som skal skrives og setter et mellomrom.
# Dersom man skirver tretti i stedetfor 30, kommer det valueerror fordi vi endret datatypen tidligere til integer, da er ikke datatypen string lengre. Det finnes metoder som gjør at den også kan godta flere "ord".