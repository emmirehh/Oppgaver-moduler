def hilsen(navn):
    print(f"Hei, {navn}!")

hilsen("Michael")
hilsen("Emmi")
hilsen("Mia")


brukerens_navn = input("Hva heter du? ")
def hilsen(brukerens_navn, alder):
    print(f"Hei, {brukerens_navn}! Du er {alder} år!")

hilsen(brukerens_navn, 31)
hilsen(31, "Michael")                             
hilsen(alder=31, brukerens_navn="Michael")        

def hilsen(navn, alder, by="Oslo"):
    print(f"Hei, {navn}! Du er {alder} år og bor i {by}!")

hilsen("Michael", 31, "Oslo")
hilsen("Michael", 31)


#---Refleksjon---
# Steg 4: Da kommer det Hei, 31! Du er Michael år! Fordi argumentene er byttet om. Det er viktig å passe på rekkefølgen på argumentene når man kaller prosedyren.
# Steg 5: Dersom man kaller prosedyren med bare et argument, vil man få TypeError fordi prosedyren forventer to argumenter.
# Steg 6: Man kan også si hvilken parameter hvert argument hører til, navngitte argumenter. Da kan man bytte på rekkefølgen på argumentene. Det kan være nyttig dersom man har mange parametere i en prosedyre, og vil gjøre det tydeligere. Standard verdi. Valgfri rekkefølge.
# Dersom man flytter by="Oslo" først i parameterlisten, vil man få SyntaxError fordi man ikke kan ha parametere med standardverdi før parametere uten standardverdi.

# Parameter er en plassholder i definisjonen. navn og alder er parametere. Argument er verdien man sender inn når man kaller prosedyren. argumenter er "Michael" og 31.
# Steg 2: Variabelen het noe annet enn parameteren, og det fungerte. Det er fordi parameteren er en plassholder. Det er forholdet mellom dem. Argumentet blir knyttet til parameteren.
