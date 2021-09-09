# Solicitatie Opdracht door Tobias Kooijman 99068704
# Intro

print("Goedemiddag/morgen")
print("Wat fijn dat je wilt soliciteren bij Vuilnis'n co.")
print("voor dat je kan gaan soliciteren, moet je nog voldoen aan een paar eisen")
print("er staat hieronder een vragenlijst, antwoord eerlijk")
print("")
PT_Erv = input("Hoeveel jaar praktijkervaring heeft uw met dierendressuur? ")

print("")

erv = 0
if PT_Erv < str(4):
    print("Helaas,je hebt minimaal 4 jaar praktijkervaring nodig om hier to soliciteren.")

if PT_Erv >= str(4):
    erv = 1
else:
    print("dit is geen geldig antwoord")

if erv == 1:

    PT_Erv_01 = input('hoeveel jaar ervaring met jongleren heb je? ')

print("")
WE5 = 0
if int(PT_Erv_01) < int(5):
    print("Helaas,je hebt minimaal 5 jaar werkervaring met jongleren nodig om hier to soliciteren.")

elif int(PT_Erv_01) >= int(5):
    WE5 = 1
else:
    print("dit is geen geldig antwoord")

acro = 0
Pt_Erv_01 = 0
PTE = 0
if WE5 == 1:
    PTE = input('hoeveel jaar ervaring acrobiek heeft u? ')

if int(PTE) < int(3):
    print("Helaas,je hebt minimaal 3 jaar acrobatiek nodig om hier to soliciteren.")

elif int(PTE) >= int(3):
    Acro = 1
else:
    print("dit is geen geldig antwoord")
Dipl = 0
if Acro == 1:
    MBO = input('heeft u een Mbo diploma? (Ja/Nee) ')
    if (MBO.lower() =="ja"):
        Dipl = 1
    elif (MBO.lower() =="nee"):
        print("Helaas,je hebt een MBO-diploma nodig om hier to soliciteren.")

VWRBW = 0

if Dipl == 1:
    RBW = input('heeft u een geldig vrachtwagen rijbewijs? (Ja/Nee) ')
    if (RBW.lower() =="ja"):
        VWRBW = 1
    elif (RBW.lower() =="nee"):
        print("Helaas,je hebt een geldig vrachtwagen rijbewijs nodig om hier to soliciteren.")

HGGH = 0

if VWRBW == 1:
    HGH = input('Bent u in het bezit van een hoge hoed? (Ja/Nee) ')
    if (HGH.lower() =="ja"):
        HGGH = 1
    elif (HGH.lower() =="nee"):
        print("Helaas,u moet in het bezit zijn van een hoge hoed om hier to soliciteren.")
gndr = 1
if HGGH == 1:
    HGH = input('Bent u een man of een vrouw? (man/vrouw) ')
    if (HGH.lower() =="man"):
        Man_01 = input('heeft u een snor? (Ja/Nee) ')
        if (Man_01.lower() =="ja"):
            Man_02 = input('Hoe breed is uw snor? (in cm) ')
            if int(Man_02) < int(10):
                print("Helaas, u heeft een snor van minimaal 10 cm nodig om hier te soliciteren")
            elif int(Man_02) < int(10):
                gndr = 1
        
        elif (Man_01.lower() =="nee"):
            print("Helaas, u heeft een snor van minimaal 10 cm nodig om hier te soliciteren")
        
    elif (HGH.lower() =="vrouw"):
        Vrouw_01 = input('draagt u rood krulhaar? (Ja/Nee) ')
        if (Vrouw_01.lower() =="ja"):
            Vrouw_02 = input('hoe lang is uw haar? (in cm) ')
            if int(Vrouw_02) < int(20):
                print("Helaas, u heeft rood krulhaar nodig van minimaal 20 cm om hier te soliciteren")
            elif int(Vrouw_02) >= int(20):
                gndr = 1
        elif (Vrouw_01.lower() =="nee"):
            print("Helaas, u heeft rood krulhaar nodig van minimaal 20 cm om hier te soliciteren")
Lang = 0
if gndr == 1:
    PTE = input('wat is uw lengte? (in cm) ')

if int(PTE) < int(150):
    print("Helaas,je moet minimaal 150cm lang zijn om hier to soliciteren.")

elif int(PTE) >= int(150):
    Lang = 1
    
if Lang == 1:
    PTE = input('wat is uw gewicht? (in kg) ')

if int(PTE) < int(90):
    print("Helaas,je moet minimaal 90kg zijn om hier to soliciteren.")

elif int(PTE) >= int(90):
    CTFC = 0
    if VWRBW == 1:
        CTFC = input('Bent u in het bezit van een certificaat overleven met gevaarlijk personeel? (Ja/Nee) ')
    if (CTFC.lower() =="ja"):
        print("Gefliciteerd!! uw bent geschikt om bij ons te soliciteren!")
    elif (CTFC.lower() =="nee"):
        print("Helaas,u moet in het bezit zijn van een certificaat overleven met gevaarlijk personeel om hier to soliciteren.")