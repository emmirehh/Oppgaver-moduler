aldersgrense = 18
alder = int(input("Hvor gammel er du: "))

if alder >= aldersgrense:
    print(f"Du er {alder} år, og gammel nok.")
else:
    print(f"Du er {alder} år, og ikke gammel nok.")

print("Takk for at du sjekket!")

#---Refleksjon---
# Jeg tror 17 år ikke er gammel nok, 18 og 19 år er gammel nok.
# Dersom man ikke har innrykket etter if statement, kommer det indentationerror.
# Dersom man ikke har kolon etter if statementen kommer det syntaxerror.
# Dersom man tar bort = i >= blir 18 år også for ungt, siden > betyr at tallet må være større i stedet for >= som betyr at det kan være likt eller større.

# Kolonet står på slutten av en linje som introduserer en ny struktur, gir beskjed om hvilke kodelinjer som hører sammen i en "blokk" med kode som hører til denne linjen. Brukes til å styre strukturen og flyten i programmet. Innrykket definerer grensene for "blokken", forteller hvilke linjer som kjøres som en del av den overstående kommandoen. Det som er utenfor if-blokken kjøres utenom, mens if kjøres dersom kriteriene inntrer.
# Steg 7 ble skrevet ut uansett alder fordi den ikke er et vilkår eller en del av if statementen.
# alder >= aldersgrense, betyr at alderen enten må være lik eller større, så dersom alderen er 18 eller høyere vil den første statementen inntre og printe du er gammel nok, men dersom alderen er mindre kommer else og meldingen ikke gammel nok, fordi det første vilkåret ikke inntreffer, da går programmet over til det neste vilkåret og handlingen som følger den.
# >= er riktig for en aldersgrense på 18 år, fordi man kan være 18 år eller eldre. Dersom man skriver > må man være over 18 år og ikke 18 som da blir for ungt. Tegnene sier litt om tallet du sammenligner med skal regnes med eller ikke.