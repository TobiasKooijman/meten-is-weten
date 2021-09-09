# Kaas Opdracht door Tobias Kooijman 99068704
#intro:
print("____________________________________________________________________________________________")
print("")
print("")
print("Welkom in het kazen spel!!")
print("kan jij raden wat voor kaas het is?")
print("")
print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
print("")

# Vraag 1:

print("vraag 1:")
kleur = input('Is de kaas geel? (Ja/Nee) ')
print("")
kleur_V = 0
if (kleur.lower() =="ja"):
    kleur_V = 1
elif (kleur.lower() =="nee"):
    kleur_v = 0
else: 
    print("                                      ERROR")
    print("Dat is antwoord is onmogelijk, start het programma opnieuw op en probeer het opnieuw!!")

# Vraag 2

smml_V = 0
gaten_V = 0
if kleur_V == 1:
    print("vraag 2:")
    gaten = input('Zitten er gaten in? (Ja/Nee) ')
    print("")
    if (gaten.lower() =="ja"):
        gaten_V = 1
    elif (gaten.lower() =="nee"):
        gaten_V = 2
    else: 
        print("                                      ERROR")
        print("Dat is antwoord is onmogelijk, start het programma opnieuw op en probeer het opnieuw!!")

elif kleur_V == 0:
    print("vraag 2:")
    gaten = input('heeft de kaas blauwe schimmels? (Ja/Nee) ')
    print("")
    if (gaten.lower() =="ja"):
        smml_V = 1
    elif (gaten.lower() =="nee"):
        smml_V = 2
    else: 
        print("                                      ERROR")
        print("Dat is antwoord is onmogelijk, start het programma opnieuw op en probeer het opnieuw!!")

#vraag 3 (Gaten)
duur_V = 0
hard_V = 0
if gaten_V == 1:
    duur_V = 0
    print("vraag 3:")
    gaten = input('is de kaas belachelijk duur? (Ja/Nee) ')
    print("")
    if (gaten.lower() =="ja"):
        duur_V = 1
    elif (gaten.lower() =="nee"):
        duur_v = 2
    else: 
        print("                                      ERROR")
        print("Dat is antwoord is onmogelijk, start het programma opnieuw op en probeer het opnieuw!!")

elif gaten_V == 2:
    print("vraag 3:")
    gaten = input('Is de kaas hard als steen? (Ja/Nee) ')
    print("")
    if (gaten.lower() =="ja"):
        hard_V = 1
    elif (gaten.lower() =="nee"):
        hard_V = 2
    else: 
        print("                                      ERROR")
        print("Dat is antwoord is onmogelijk, start het programma opnieuw op en probeer het opnieuw!!")

# Vraag 3 (schimmel)


korst1_V = 0
korst2_V = 0
if smml_V == 1:
    korst1_V = 0
    print("vraag 3:")
    gaten = input('heeft de kaas een korst? (Ja/Nee) ')
    print("")
    if (gaten.lower() =="ja"):
        korst1_V = 1
    elif (gaten.lower() =="nee"):
        korst1_V = 2
    else: 
        print("                                      ERROR")
        print("Dat is antwoord is onmogelijk, start het programma opnieuw op en probeer het opnieuw!!")

elif smml_V == 2:
    korst2_V = 0
    print("vraag 3:")
    gaten = input('heeft de kaas een korst? (Ja/Nee) ')
    print("")
    if (gaten.lower() =="ja"):
        korst2_V = 1
    elif (gaten.lower() =="nee"):
        korst2_V = 2
    else: 
        print("                                      ERROR")
        print("Dat is antwoord is onmogelijk, start het programma opnieuw op en probeer het opnieuw!!")

# Antwoorden Deel 1 (Ja bij Kleur, ja bij gaten)

if duur_V == 1:
    print("Goed Gespeeld!!")
    print("Jouw antwoord was Emmenthaler!!")
    print("")
    print("Start het programma opnieuw op om het opnieuw te proberen!!")

elif duur_V == 2:
    print("Goed Gespeeld!!")
    print("Jouw antwoord was Leerdammer!!")
    print("")
    print("Start het programma opnieuw op om het opnieuw te proberen!!")

# Antwoorden Deel 2 (Ja bij kleur, nee bij gaten)

if hard_V == 1:
    print("Goed Gespeeld!!")
    print("Jouw antwoord was Parmigiano Reggiano!!")
    print("")
    print("Start het programma opnieuw op om het opnieuw te proberen!!")

elif hard_V == 2:
    print("Goed Gespeeld!!")
    print("Jouw antwoord was Goudse Kaas!!")
    print("")
    print("Start het programma opnieuw op om het opnieuw te proberen!!")

# Antwoorden Deel 3 (Nee bij Kleur, ja bij schimmel)

if korst1_V == 1:
    print("Goed Gespeeld!!")
    print("Jouw antwoord was Parmigiano Bleu de Rochbaron!!")
    print("")
    print("Start het programma opnieuw op om het opnieuw te proberen!!")

elif korst1_V == 2:
    print("Goed Gespeeld!!")
    print("Jouw antwoord was Fourme d'Ambert!!")
    print("")
    print("Start het programma opnieuw op om het opnieuw te proberen!!")

# Antwoorden deel 4 (nee bij kleur, nee bij Schimmel)

if korst2_V == 1:
    print("Goed Gespeeld!!")
    print("Jouw antwoord was Camembert!!")
    print("")
    print("Start het programma opnieuw op om het opnieuw te proberen!!")

elif korst2_V == 2:
    print("Goed Gespeeld!!")
    print("Jouw antwoord was Mozzarella!!")
    print("")
    print("Start het programma opnieuw op om het opnieuw te proberen!!")


