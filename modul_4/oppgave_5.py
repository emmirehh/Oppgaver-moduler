riktig_svar = "Oslo"

svar = input("Hva er hovedstaden i Norge? ")

if svar == riktig_svar:
    print("Riktig!")
else:
    print("Feil, svaret var", riktig_svar)

alder = int(input("Hvor gammel er du? "))

if alder == 18:
    print("Du er akkurat myndig!")
else:
    print("Du er ikke 18.")


#---Refleksjon---
# Feilene var: Glemte == for at svaret måtte være Oslo. Glemte kolon i første if statement. Glemte innrykket med printen til else. Glemte å gjøre alder om til integer, siden det er heltall.
# Den siste feilen ga ingen feilmelding. De er en logisk feil. 18 kan også skrives som string.
# Syntaksfeil er feil som stopper programmet. Logiske feil er feil som gjør at programmet gjør noe annet enn du ville og uventet resultat. Syntaksfeil er mindre farlig fordi det er brudd på grammatikkregler eks parantes eller skrivefeil som gjør at maskinen ikke forstår koden og ikke vil gå videre, feilen er da lett å finne under utvikling. Logiske feil er ganske farlig siden koden er gyldig og kjører programmet, fordi de ikke blir oppdaget av datamaskinen og kan forbli uoppdaget og kan føre til uønskede konsekvenser.
# Det er lurt å teste med forskjellige datatyper for å finne logiske feil i et program.