import random
import time



name = input("Hey, na wer spielt denn heute mit mir?")

print("Ah, hey ", name)

print("Los gehts, ", name)


def stelle_fragen(fragedaten):
    ausgewahlte_frage = random.choice(fragedaten)
    frage = ausgewahlte_frage["Frage"]
    antwort = ausgewahlte_frage["Antwort"]

    antwort_frage = input(f"{frage} ").lower()
    time.sleep(1)

    if antwort_frage == antwort.lower():
        print("Das richtig!")
        time.sleep(1)
        return 10


    else:
        print("leider falsch")
        time.sleep(1)
        return 0

fragen_liste = [

    {"Frage":"Was ist die Hauptstadt von Deutschland?", "Antwort":"berlin"},
    {"Frage":"Ist es Nachts dunkel?", "Antwort": "Ja"},
    {"Frage":"Welche Haarfarbe hat die Linda?", "Antwort": "Rot"},
    {"Frage":"Ist Metallica eine Band?", "Antwort": "Ja"},
    {"Frage":"Welches Tier sieht aus wie ein Pferd, hat aber streifen? Ein...", "Antwort": "Zebra"},
    {"Frage":"Was ist das Wahrzeichen von Köln?", "Antwort":"Dom"},
    {"Frage":"Ist Bier gesund?", "Antwort" : "ja"},
    {"Frage": "Wer hat denn Heute Geburtstag?", "Antwort": "Silke"},
    {"Frage": "Ist die Sonne sehr heiß?", "Antwort": "Ja"},
    {"Frage": "Aus was besteht Wein?", "Antwort": "Trauben"},

]


punkte = 0
ausgewahlte_frage = None

while punkte < 100 and fragen_liste:
    punkte += stelle_fragen(fragen_liste)

    if punkte == 100:
        print("Herzlichen Glückwunsch, du hast es geschafft. Du bist ein wahrer Gewinner")
        quit()

    print("Punktestand: ", punkte)

