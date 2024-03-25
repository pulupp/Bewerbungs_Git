grocery_list = {}

# Eingabeaufforderung für den Benutze

# Eingabe von Artikel hinzufügen
while True:
    try:
        item = input("").strip()

        # Überprüfen, ob der Benutzer "exit" eingegeben hat
        if item.lower() == 'exit':
            break

        # Artikel zur Einkaufsliste hinzufügen (in Großbuchstaben)
        grocery_list[item.upper()] = grocery_list.get(item.upper(), 0) + 1
    except EOFError:
        print("\n")
        break

#infinate loop
for item, count in sorted(grocery_list.items()):
#print list in upper alphabetisch und anzahl an items
    print(f"{count} {item}")
#exit with