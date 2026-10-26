#alder = 25
#er_student = True
#har_medlemskort = False

# Jeg tror det blir: False. Ble False. Alderen er ikke er mindre enn 12 og den er ikke mer enn 67.
#print(alder < 12 or alder > 67)

# Jeg tror det blir: True. Ble True. er_student = True og alderen er mindre enn 30.
#print(er_student and alder < 30)

# Jeg tror det blir: True. Ble True. har_medlemskort er egentlig False, men siden not snur verdien, blir den True i stedet.
#print(not har_medlemskort)

# Jeg tror det blir: False. Ble False. Det er kun den ene som er True og ikke begge, derfor blir den False.
#print(er_student and har_medlemskort)

# Jeg tror det blir: True. Ble True. Er True dersom minst en av sidene er sann.
#print(er_student or har_medlemskort)

# Jeg tror det blir: True. not er_student gjør den til False i stedet for True, men alderen er fremdeles under 30 og True, så den ene stemte og gjorde det til True.
#print(not er_student or alder < 30)


alder = int(input("Alder: "))
er_student = input("Er du student? (ja/nei) ").lower() == "ja"

if alder < 12 or alder > 67:
    print(f"Gratis")
elif er_student and alder < 30:
    print(f"Det blir 50 kr")
else:
    print(f"Det blir 120 kr")

if not er_student:
    print("Studenter under 30 år får rabatt")


#---Refleksjon---
# 8 år, ikke student: Tror Gratis. Ble gratis og fikk tips om at studenter får rabatt.
# 70 år, ikke student: Tror Gratis. Ble gratis of fikk tips om at studenter får rabatt.
# 22 år, student: Tror 50 kr. Ble 50.
# 35 år, student: Tror 120 kr. Ble 120.
# 25 år, ikke student: Tror 120 kr og får tips om at studenter får rabatt. Ble det samme.

# Må skrive med små bokstaver/ nøyaktig før utvidelsen for å få riktig svar, ==. .lower gjør svaret om til små bokstaver, slik at brukeren kan skrive det med store og små bokstaver.
# and betyr at begge må være True. Med or må bare en av alternativene stemme for at det skal bli True.
# 35 åringen som er student fikk 120 kr i pris fordi personen er over 30 år, som vil si at personen ikke får rabatt.
# not, gjør True til False, og False til True. Kunne skrevet if er_student == False: .Print.
# Dersom en 70 åring som også er student, vil den første if statementen slå til og stopper der. Dersom man for eksempel hadde skrevet ordinær pris først hadde den slått til i stedet. 