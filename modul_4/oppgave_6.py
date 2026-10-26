riktig_brukernavn = "michael"
riktig_passord = "python123"

brukernavn = input("Brukernavn: ")
passord = input("Passord: ")
alder = int(input("Alder: "))

if brukernavn == riktig_brukernavn and passord == riktig_passord and alder < 13:
    print("Du er for ung")

elif brukernavn == riktig_brukernavn and passord == riktig_passord:
    print(f"Velkommen, {riktig_brukernavn}!")

elif brukernavn == riktig_brukernavn:
    print("Feil passord.")

elif brukernavn != riktig_brukernavn:
    print("Ukjent bruker.")

else:
    print("Ukjent bruker")

#---Refleksjon---
# Riktig brukernavn, riktig passord: Jeg tror man kommer seg inn. Den stemte.
# Riktig brukernavn, feil passord: Da kommer det opp Feil passord. Den stemte.
# Feil brukernavn, riktig passord: Da kommer det Ukjent bruker. Den stemte.
# Feil brukernavn, feil passord: Da kommer det Ukjent bruker. Den stemte.

# Jeg brukte and for å løse oppgaven. 
# Det må være i den rekkefølgen for at logikken skal gå gjennom. Dersom man endrer rekkefølgen vil en av de andre utfylle kriteriene. 
# På grunn av sikkerhet. For da kan man vite om brukernavnet eller passordet er i bruk.
# Lurt å teste alle kombinasjonene fordi det kan være logiske feil. Sjekke at alt fungerer som det skal.