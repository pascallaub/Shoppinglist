list = []

def add_item():
    item = input("Bitte gib den Artikel ein, der zu Einkaufsliste hinzugefügt werden soll: ")
    if item == '':
        None
    else:
        list.append(item)
        print(f"{item} erfolgreich hinzugefügt!")
        weiterer_artikel = input("Möchtest du einen weiteren Artikel eingeben? j/n: ")
        if weiterer_artikel == 'j':
            add_item()
        else:
            None

def show_shoppinglist():
    if list == []:
        print("Noch keine Artikel hinzugefügt.")
    else:
        for item in list:
            print(item)

def sorted_list():
    sortierte_liste = sorted(list)
    for item in sortierte_liste:
        print(item)

def del_item():
    for item in list:
        print(item)
    suche = input("Welchen Artikel möchtest du löschen? ")
    list.remove(suche)
    print("Artikel erfolgreich entfernt!")

def menu():
    while True:
        print("-----Einkaufsliste-----")
        print("1. Artikel hinzufügen")
        print("2. Einkaufsliste anzeigen")
        print("3. Artikel sortieren")
        print("4. Artikel löschen")
        print("5. Programm beenden")
        choice = input("1, 2, 3, 4 oder 5: ")
        if choice == '1':
            add_item()
            continue
        elif choice == '2':
            show_shoppinglist()
            continue
        elif choice == '3':
            sorted_list()
            continue
        elif choice == '4':
            del_item()
            continue
        elif choice == '5':
            break
        else:
            print("Falsche Eingabe!")
            continue

if __name__=="__main__":
    menu()
